#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket, pickle

class Client:
    def __init__(self, host='localhost', port=1234):
        self.sock = socket.socket()
        self.sock.connect((host, port))

    def send(self, s):
        #print("Socket: A enviar:", s)
        self.sock.send(s.encode())

    def recv(self):
        rec = self.sock.recv(1024)
        tagged = pickle.loads(rec)
        print("Analise:", tagged)
        return tagged

    def close(self):
        self.sock.close()