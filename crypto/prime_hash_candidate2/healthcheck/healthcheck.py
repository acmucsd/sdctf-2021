#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pwnlib, sys
from typing import List

# def handle_pow(r):
#     print(r.recvuntil(b'python3 '))
#     print(r.recvuntil(b' solve '))
#     challenge = r.recvline().decode('ascii').strip()
#     p = pwnlib.tubes.process.process(['kctf_bypass_pow', challenge])
#     solution = p.readall().strip()
#     r.sendline(solution)
#     print(r.recvuntil(b'Correct\n'))

PROCESS = pwnlib.tubes.remote.remote('127.0.0.1', 1337)
# print(r.recvuntil('== proof-of-work: '))
# if r.recvline().startswith(b'enabled'):
#     handle_pow(r)

PASSWD = 91918419847262345220747548257014204909656105967816548490107654667943676632784144361466466654437911844
TEST = 102600138716356059007219996705144046117627968461
PRIME = 1

# On Unix systems (Ex. Linux), newline terminates the input line so it cannot be included as part of the line
NEWLINE_CODEPOINT = ord('\n')

def crack_hash(hsh: int) -> bytes:
    byts_reversed: List[int] = []
    while hsh > 0:
        byts_reversed.append(hsh % PRIME)
        hsh //= PRIME
    for i in range(len(byts_reversed)):
        codepoint = byts_reversed[i]
        if codepoint == NEWLINE_CODEPOINT:
            byts_reversed[i] += PRIME
            if i+1 < len(byts_reversed) and byts_reversed[i+1] > 0:
                byts_reversed[i+1] -= 1
            else:
                # This rarely happens on random hashes
                #raise RuntimeError("Unable to crack!")
                return chr(0).encode()
    try:
        return bytes(reversed(byts_reversed))
    except:
        return chr(0).encode()

secre1 = ""
secret2 = ""

for i in range (101, 997):
    PRIME = i
    try:
        a = crack_hash(TEST).decode()
        if a.isprintable():
            # should only be one
            secret2 = a
            break
    except:
        pass

a = 'a' * 20
PROCESS.recvline()
PROCESS.sendline(a)
hash = PROCESS.recvline().decode().split()[4]
secret1 = crack_hash(int(hash)).decode()[0:20]
secret1 = "".join([chr(ord(x) ^ ord(y)) for x,y in zip(a,secret1)])

possible_passwords = []

for i in range(1,10):
    password = crack_hash(PASSWD)
    password = [chr(x ^ ord(y)) for x,y in zip(password,secret1[0:i]*len(password))]
    password = "".join(password)[:-20]
    if password.isprintable():
        possible_passwords.append(password)

for p in possible_passwords:
    print('Trying: {}'.format(p))
    print('Response:', PROCESS.recvline())
    PROCESS.sendline(p)
    check = PROCESS.recvline()[:-1].decode()
    if "Login" in check:
        flag = PROCESS.recvline()[:-1].decode()
        if flag == 'Flag: sdctf{W0W_s3cur1ty_d1d_dRaStIcAlLy_1mpr0v3}':
            print('Health check passed!')
            exit(0)
        else:
            print('Incorrect flag: {}'.format(flag))
            exit(1)

print('[!]: No possible passwords!', file=sys.stderr)
exit(1)
