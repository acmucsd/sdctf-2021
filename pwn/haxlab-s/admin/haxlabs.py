#! /usr/bin/env python3
import traceback, sys
from typing import Any, Dict
from seccomp import SyscallFilter, TRAP, ALLOW, Arg, EQ, ERRNO
from errno import EPERM

PROMPT = '>>> '

def load_modules():
    # Preload some modules since we would have no file access after seccomp
    # No way a hacker can escape with those since most syscalls would result in EPERM
    print('Loading modules...')
    import posix, pwd, spwd, grp, crypt, termios, tty, pty, fcntl, pipes, resource, nis, syslog
    print('Done')

# Use an incredibly restrictive syscall whitelist!
# there is NO way a hacker can do anything except basic console input/output
def init_seccomp():
    f = SyscallFilter(defaction=ERRNO(EPERM))

    f.add_rule(ALLOW, "rt_sigaction")
    f.add_rule(ALLOW, "rt_sigreturn")
    f.add_rule(ALLOW, "exit_group")
    f.add_rule(ALLOW, "brk")

    f.add_rule(ALLOW, "read", Arg(0, EQ, sys.stdin.fileno()))
    f.add_rule(ALLOW, "ioctl", Arg(0, EQ, sys.stdin.fileno()))

    f.add_rule(ALLOW, "write", Arg(0, EQ, sys.stdout.fileno()))
    f.add_rule(ALLOW, "ioctl", Arg(0, EQ, sys.stdout.fileno()))

    f.add_rule(ALLOW, "write", Arg(0, EQ, sys.stderr.fileno()))
    f.add_rule(ALLOW, "ioctl", Arg(0, EQ, sys.stderr.fileno()))

    f.load()

# Drop the user into a REPL
def repl():
    global_dict: Dict[str,Any] = dict()
    while True:
        try:
            src = input(PROMPT)
        except EOFError:
            print()
            break
        if src == '':
            continue
        try:
            code = compile(src, '<string>', 'single')
        except SyntaxError:
            traceback.print_exc()
            continue
        try:
            exec(code, global_dict)
        except Exception:
            traceback.print_exc()

load_modules()
init_seccomp()
repl()
