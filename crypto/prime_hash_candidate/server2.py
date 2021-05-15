#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 65432
ERROR = "Wrong password, try again\n"
SUCCESS = "Login successful!\nFlag: sdctf_ok_test\n"
PASSWD = "59784015375233083673486266"

def hash(data):
    out = 0
    for c in data:
        out *= 31
        out += ord(c)
    return str(out)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            conn.sendall("Please enter password below\n".encode('utf-8'))
            while True:
                data = conn.recv(1024).decode()
                if not data:
                    break
                if hash(data) == PASSWD:
                    conn.sendall(SUCCESS.encode('utf-8'))
                    break
                else:
                    conn.sendall(ERROR.encode('utf-8'))
