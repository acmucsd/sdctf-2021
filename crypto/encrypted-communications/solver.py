#! /usr/bin/env python2
# Usage: ./solver.py HOST PORT
import sys
import base64
import hashlib
import re
import string

import itertools

from crypto_commons.netcat.netcat_commons import receive_until_match, nc, send, receive_until
from crypto_commons.symmetrical.symmetrical import set_byte_cbc, set_cbc_payload_for_block


def pad(msg):
    pad_length = 16 - len(msg) % 16
    return msg + chr(pad_length) * pad_length


def gen_payload(encrypted, plaintext, new_payload):
    raw = encrypted.decode("base64")
    new_payload = pad(new_payload)[:16]
    plaintext = ("\0" * 16) + (pad(plaintext)[:16])
    payload = set_cbc_payload_for_block(raw, plaintext, new_payload, 1)
    return base64.b64encode(payload)

if len(sys.argv) <= 2:
    print 'usage: ./solve.py HOST PORT'

# HOST = "localhost"
# PORT = 9999
HOST = sys.argv[1]
PORT = int(sys.argv[2])

def main():
    f = 0
    encrypted_flag = ""
    welcome = ""

    while f == 0:
        s = nc(HOST, PORT)
        welcome = receive_until(s, "\n")[:-1]
        print("welcome: ", welcome[:-1])
        # Get command not found
        send(s, welcome)
        receive_until(s, "\n")
        receive_until(s, "\n")
        cnf = receive_until(s, "\n")[:-2]
        print("cnf: ", cnf)
        payload = gen_payload(welcome,"Welcome!","get-flag")
        receive_until(s, "\n")
        send(s, payload)
        receive_until(s, "\n")
        encrypted_flag = receive_until(s, "\n")[:-2]
        payload = gen_payload(encrypted_flag,"send_flag_","get-flag\x00\x00")
        send(s, payload)
        receive_until(s, "\n")
        encrypted_flag2 = receive_until(s, "\n")[:-2]
        print("encrypted flag: ", encrypted_flag2)
        print
        if encrypted_flag2 != cnf:
            f = 1
            break

    raw_enc_flag = encrypted_flag.decode("base64")
    flag = ""
    current = "send_fl"
    print('encrypted flag', encrypted_flag, encrypted_flag.decode("base64"), len(encrypted_flag.decode("base64")))
    for block_to_recover in range(3):
        malleable_block = base64.b64encode(raw_enc_flag[block_to_recover * 16:])
        missing = 16 - len(current)
        for spaces in range(missing):
            for c in string.printable:
                test_flag_block_prefix = current + c + ("\0" * (missing - spaces))
                expected_command = (" " * spaces) + "get-flag"
                payload = gen_payload(malleable_block, test_flag_block_prefix, expected_command)
                send(s, payload)
                receive_until(s, "\n")
                result = receive_until(s, "\n")[:-2]
                if result == encrypted_flag:
                    current += c
                    print('found matching flag char:', current)
                    break
        print("current:", current)
        flag += current
        known_blocks = raw_enc_flag[16 * block_to_recover:16 * block_to_recover + 32]
        expanded_flag = raw_enc_flag[16 * block_to_recover:] + known_blocks
        next_block_known = ""
        for i in range(8):
            get_md5 = set_cbc_payload_for_block(expanded_flag, "\0" * 16 + current, (" " * 9) + "get-md5", 1) # first block is get-md5
            get_md5 = set_byte_cbc(get_md5, ("\0" * (5 - block_to_recover) * 16) + current,
                                   (6 - block_to_recover) * 16 - 1, chr((4 - block_to_recover) * 16 - i - 1)) # last character to cut padding
            send(s, base64.b64encode(get_md5))
            receive_until(s, "\n")
            real_md5_result = receive_until(s, "\n")[:-2]
            for c in string.printable:
                test_md5_payload = set_cbc_payload_for_block(expanded_flag, "\0" * 16 + current,
                                                             (" " * (8 - i - 1)) + "get-md5" + next_block_known + c, 1)
                test_md5_payload = set_byte_cbc(test_md5_payload, ("\0" * (5 - block_to_recover) * 16) + current,
                                                (6 - block_to_recover) * 16 - 1,
                                                chr((4 - block_to_recover) * 16 + 1))
                send(s, base64.b64encode(test_md5_payload))
                receive_until(s, "\n")
                test_md5_result = receive_until(s, "\n")[:-2]
                if real_md5_result == test_md5_result:
                    next_block_known += c
                    print('found matching flag char:', next_block_known)
                    if c == '}':
                        print(flag+next_block_known)
                        exit(0)
                    break
        print(next_block_known)
        print(flag)
        current = next_block_known[:-1]


main()
