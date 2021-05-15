# from pwnlib.tubes import remote
# p = remote.remote('<host>', <port>) # If connecting to remote
from pwnlib.tubes import process
p = process.process(['python3', 'server_admin.py'], cwd='challenge/')
print(p.recv().decode())
f = open("collision1.bin","rb")
f2 = open("collision2.bin","rb")
p.sendline(b'ls')
# Test for robustness
# import time
# p.send(b'l')
# print('First part sent')
# time.sleep(1)
# p.sendline(b's')
# print('Second part sent')
# Test for robustness end
print(p.recv().decode()) # TODO: make this robust on networks by reading until a character
p.sendline(f.read())
print(p.recv().decode())
p.sendline(f2.read())
print(p.recv().decode())
# p.close()

p.interactive()
