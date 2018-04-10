#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket, pickle

class Client:
    def __init__(self, host='localhost', port=1234):
        self.sock = socket.socket()
        self.sock.connect((host, port))
        print("Ligado ao servidor.")

    def Tokenize(self, frase):
        self.sock.send(pickle.dumps({'token': frase}))
        recv = self.sock.recv(1024)
        loaded = pickle.loads(recv)
        print("Tokenize:", loaded)
        return loaded

    def PoS(self, frase):
        self.sock.send(pickle.dumps({'pos': frase}))
        recv = self.sock.recv(1024)
        loaded = pickle.loads(recv)
        print("PoS:", loaded)
        return loaded

    def Split(self, frase):
        self.sock.send(pickle.dumps({'split': frase}))
        recv = self.sock.recv(1024)
        loaded = pickle.loads(recv)
        print("Split:", loaded)
        return loaded

    def close(self):
        self.sock.close()