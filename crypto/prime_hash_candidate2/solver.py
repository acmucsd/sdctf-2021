from pwnlib.tubes import process

from typing import List

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

# Run locally, for remote connection replace with
# from pwnlib.tubes import remote
# PROCESS = remote.remote('<host>', <port>)
PROCESS = process.process(['python3', 'challenge/server_admin.py'])

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
    PROCESS.recvline()
    PROCESS.sendline(p)
    check = PROCESS.recvline()[:-1].decode()
    if "Login" in check:
        print(PROCESS.recvline()[:-1].decode())
