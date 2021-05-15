#! /usr/bin/env python3
from pwnlib.tubes import remote

# Get from solver-static.py
STATIC_INPUT_PASSWORD = b'\x02\x14\x05\x17\x17\x1b\x13\x16\t\x04\x0c\x05\x17\x0c\r\x12\x08)'

PROCESS = remote.remote('localhost', 1337)

print(PROCESS.recvuntil(b'Please enter password below\n'))

# print('Sending cracked password...')

PROCESS.sendline(STATIC_INPUT_PASSWORD)

# print('Password sent')

line = PROCESS.recvline(keepends=False)
print(line)

if line == b'Login successful!':
    print(PROCESS.recvuntil(b'sdctf{'))
    print(PROCESS.recvuntil(b'}'))
    exit(0)
else:
    print('No flag for me :(')
    exit(1)
