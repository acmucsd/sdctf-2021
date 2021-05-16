#!/usr/bin/env python3

ERROR = "Wrong password, try again\n"
SUCCESS = "Login successful!\nFlag: sdctf{st1ll_3553nt14lly_pl@1n_txt}\n"
PASSWD = "59784015375233083673486266"

def hash(data):
    out = 0
    for c in data:
        out *= 31
        out += ord(c)
    return str(out)

data = input("Please enter password below\n")

try:
    while True:
        if hash(data) == PASSWD:
            print(SUCCESS)
            break
        else:
            data = input(ERROR)
except EOFError:
    pass
