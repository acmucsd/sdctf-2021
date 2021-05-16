# HAXLAB S
## Pwn - Hard
| author | prereq chals | first blood | solves | final points |
| --- | --- | --- | --- | --- |
| k3v1n | none | **ptr-yudai** from **Team zer0pts** | 1 | 996 |

### prompt
PwnWorks just released a patch for HAXLAB. The developers realized that the ultimate solution to RCEs is Linux's secure computing mode and claimed that the program is immune to pwns. Indeed, the program is so secure that it dares showing off its bash prompt.

Connect via: `nc haxlab-s.sdc.tf 1337`

### original specification
A much more difficult Python jail. Using seccomp (ban open and use a restrictive whitelist to be determined). (Note: when the program calls an illegal syscall "Bad system call" and crashes print a message like "Syscall permission denied" to make it slightly easier)

launch script is unbuffer bash -c './haxlabs.py < network-in; bash' > network-out

After the user try to exit ./haxlabs.py, he/she will not be able to access bash since it is does not read input from the network. A comment line in the shell script can be: "When our attackers have given up, show off our beautiful and fancy bash shell prompt to them to make them jealous."

The vulnerability can be TIOCSTI ioctl (See man page ioctl_tty(2))on a tty shared with an internal bash shell. See https://ruderich.org/simon/notes/su-sudo-from-root-tty-hijacking

Possible hints (give when there are 0 solves):
- Why do we run a bash shell?
- Why use unbuffer instead of passing the interactive flag to bash
- A similar vulnerability exists in su, sudo, and bubblewrap

The only way to get out is to communicate with another program is via a method in Python (can be found using dir() in Python) called communicate, which internally writes to and read from a pair of FIFOs already opened. The program on the outside is vulnerable. At least allow a way to dump the outside program's binary executable in base64.

See https://lwn.net/Articles/634391/ for how to setup seccomp in Python. Debian has a package for that called python3-libseccomp.

**flag**: `sdctf{h1st0ry_r3peat1ng:CVE-2017-5226}`
### writeups
- https://hackmd.io/@ptr-yudai/BJ3BCl8dd#HAXLAB-S
