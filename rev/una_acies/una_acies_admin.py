#! /usr/bin/env python2
from __future__ import print_function
import sys

def ok(test):
    x = 5
    for i in range(43):
        x = x | i ^ i*x + x
    return x

def test2():
    return str(ok(2))

def no():
    k = 3
    for a in range(23):
        k = k | a*a << a%k*a ^ a*k
    return str(k)

def why(a,b):
    return "".join([chr(ord(x) ^ ord(y)) for x,y in zip(str(a),b)])

def test(what):
    b = no()
    d = ok(5)
    j = test2()
    return ("nope", flag)[why(why(what,no()),test2()) == secret]

secret = "7<`+'eX#&QcZ1zVrr2's`%>}B7"
flag = open("flag.txt").read()

try:
    while(True):
        print("Enter key: ", end="")
        sys.stdout.flush()
        u = raw_input()
        print(test(u))
        sys.stdout.flush()
except EOFError:
    pass
