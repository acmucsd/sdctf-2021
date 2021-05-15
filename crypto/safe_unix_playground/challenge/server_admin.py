#!/usr/bin/env python3

import subprocess
import hashlib
import base64
import sys
import binascii

ERROR = "Invalid command with hash "
BASE64_COMMAND = b'b64'

# Some nice sample commands, can be ran without the premium plan
whitelist_commands = ['ls', 'cat flag-1.txt']
hashes = list(map(lambda cmd: hashlib.md5(cmd.encode()).hexdigest(), whitelist_commands))
hashes2 = []

def check(cmd: bytes):
    stripped = cmd.split(b'#',1)[0].strip()
    if hashlib.md5(stripped).hexdigest() in hashes:
        hashes2.append(hashlib.md5(cmd).hexdigest())
        try:
            return subprocess.check_output(stripped, shell=True)
        except:
            return
    elif hashlib.md5(cmd).hexdigest() in hashes2:
        try:
            return subprocess.check_output(stripped, shell=True)
        except:
            return

print("Welcome to the secure playground! Enter commands below")
while True:
    sys.stdout.flush()
    # data = os.read(0, 1024) # May break on very slow networks where one single payload is broken into multiple pieces, not tested with xinetd
    data = sys.stdin.buffer.readline() # May break if the payload (MD5 collision) contains a newline character \x0a
    # print(data)
    if data == b'': # EOF
        sys.exit()
    if data.strip() == BASE64_COMMAND:
        print('Enter command in base64> ', end='', flush=True)
        # base64_command = input('Enter command in base64> ')
        base64_command = sys.stdin.buffer.readline().strip()
        try:
            data = base64.b64decode(base64_command, validate=True)
        except binascii.Error as e:
            print('ERROR: Invalid base64: {}'.format(e))
            continue
    # print('[*]: data {}'.format(data))
    result = check(data)
    if result:
        print(result.decode())
    else:
        print(ERROR + hashlib.md5(data).hexdigest() + "\n")
