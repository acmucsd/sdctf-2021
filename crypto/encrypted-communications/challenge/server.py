#!/usr/bin/env python2.7

from Crypto.Hash import *
from Crypto.Cipher import AES
import os, base64, time, random, string, sys

BLOCK_SIZE = 16
KEY = os.urandom(16)
IV = os.urandom(16)

def pad(msg):
    pad_len = BLOCK_SIZE - len(msg) % BLOCK_SIZE
    return msg+chr(pad_len)*pad_len

def unpad(msg):
    return msg[:-ord(msg[-1])]

def encrypt(iv,msg):
    msg = pad(msg)
    cipher = AES.new(KEY,AES.MODE_CBC,iv)
    encrypted = cipher.encrypt(msg)
    return encrypted

def decrypt(iv,msg):
    cipher = AES.new(KEY,AES.MODE_CBC,iv)
    decrypted = cipher.decrypt(msg)
    decrypted = unpad(decrypted)
    return decrypted

def send_msg(msg):
    encrypted = encrypt(IV,msg)
    msg = IV+encrypted
    msg = base64.b64encode(msg)
    print msg
    sys.stdout.flush()
    return

def recv_msg():
    msg = raw_input()
    try:
        msg = base64.b64decode(msg)
        assert len(msg)<500
        decrypted = decrypt(msg[:16],msg[16:])
        return decrypted
    except:
        return "ERROR"

if __name__ == "__main__":
    with open("flag.txt") as fd:
        flag = fd.read()
    flag_size = len(flag)

    insertion_range = flag_size
    insertion_position = random.randrange(insertion_range)
    flag2 = flag[:insertion_position] + "send_flag_" + flag[insertion_position:]

    send_msg("Welcome!!")

    while True:
        try:
            msg = recv_msg().strip()
            if msg.startswith('get-flag'):
                send_msg(flag2)
            elif msg.startswith('get-md5'):
                send_msg(MD5.new(msg[7:]).digest())
            elif msg.startswith('get-time'):
                send_msg(str(time.time()))
            elif msg.startswith('get-sha1'):
                send_msg(SHA.new(msg[8:]).digest())
            elif msg.startswith('get-sha256'):
                send_msg(SHA256.new(msg[10:]).digest())
            else:
                send_msg('command not found')
        except:
            exit(0)
