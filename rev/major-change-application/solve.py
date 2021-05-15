#! /usr/bin/env python3
from typing import List, Optional
import random, string, pwnlib.tubes, time, ctypes

MASK_32BIT = 0xFFFF_FFFF
MASK_64BIT = 0xFFFF_FFFF_FFFF_FFFF
HASH_INIT = 0xc0de5bad13375eed
HASH_PRIME = 31

N = 2

def hasher_unsigned(first_last_name: str, mask, init: int=HASH_INIT) -> int:
    """The hash function to hash the combined first + last name into a check value"""
    h = init
    for c in first_last_name:
        h = (h * HASH_PRIME + ord(c)) & mask
    return h

# assume hash is positive
def dehash(h: int, init: int=HASH_INIT) -> Optional[str]:
    res: List[str] = []
    while h > init:
        # assumes that result has codepoint in [N*HASH_PRIME,(N+1)*HASH_PRIME)
        # include 0-9 and dash '-'
        # guarantee printability
        codepoint = h % HASH_PRIME + N * HASH_PRIME
        res.append(chr(codepoint))
        h = (h - codepoint) // HASH_PRIME
    return ''.join(reversed(res)) if h == init else None

SUFFIX_LENGTH = 12

def crack_hash(hsh: int) -> str:
    """Find a readable string that hashes to `hsh` by `hasher_unsigned()`"""
    while True:
        prefix = ''.join(random.choice(string.ascii_letters) for _ in range(5))
        prefixed_template = prefix + '\0' * SUFFIX_LENGTH
        hash_minor = (hsh - hasher_unsigned(prefixed_template, MASK_64BIT)) & MASK_64BIT
        s = dehash(hash_minor, init=0)
        if s != None and len(s) == SUFFIX_LENGTH:
            # print(s, rhash)
            return (prefix + s)

def main():
    random.seed(1337) # Fixed seed for reproduce-ability
    # change to remote to test remote functionality
    target = pwnlib.tubes.process.process("./chal.out")
    # target = pwnlib.tubes.remote.remote("localhost", <port>)
    required_hash = int(time.time()) // 4
    # required_hash = 404159631
    print('[*] Time since epoch // 4: {}'.format(required_hash))
    firstname_lastname = crack_hash(required_hash)
    print('[*] First + last name : {}'.format(firstname_lastname))
    # Present on glibc Linux platforms, need that for rand()/srand() calculation
    libc = ctypes.CDLL('libc.so.6')
    libc.srand(hasher_unsigned(firstname_lastname, MASK_32BIT, init=0))
    student_id_number = libc.rand() % 1_0000_0000
    target.sendline(firstname_lastname[1:] + ', ' + firstname_lastname[:1]) # Enter in Last, First format
    target.sendline('H{:08}'.format(student_id_number))
    target.sendline('yeet')
    target.interactive()

if __name__ == "__main__":
    main()
