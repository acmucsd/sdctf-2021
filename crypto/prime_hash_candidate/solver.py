from pwnlib.tubes import process

from typing import List

PASSWD = 59784015375233083673486266
PRIME = 31

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
                raise RuntimeError("Unable to crack!")
    return bytes(reversed(byts_reversed))

# Run locally, for remote connection replace with
# from pwnlib.tubes import remote
# PROCESS = remote.remote('<host>', <port_number>)
PROCESS = process.process(['python3', 'server_admin.py'])

print('Sending cracked password...')
# print(crack_hash(PASSWD))
PROCESS.sendline(crack_hash(PASSWD))

print('Password sent')
PROCESS.interactive()
