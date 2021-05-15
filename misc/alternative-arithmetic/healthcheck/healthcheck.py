#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pwnlib, os

FLAG_1 = b"sdctf{JAVA_Ar1thm3tIc_15_WEirD}"
FLAG_2 = b"sdctf{MATH_pr0f:iS_tH1S_@_bUG?CS_prOF:n0P3_tHIS_iS_A_fEATuRe!}"

with open(os.path.dirname(os.path.realpath(__file__)) + '/sample-solution.txt') as sf:
    solution = sf.read()

r = pwnlib.tubes.remote.remote('localhost', 1337)
r.send(solution)
print('Solution sent')
print(r.recvuntil(FLAG_1))
print('Flag 1 received')
print(r.recvuntil(FLAG_2))
print('Flag 2 received')

exit(0)
