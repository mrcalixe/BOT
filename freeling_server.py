#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, socket, pickle
import multiprocessing as mp
from Wrappers.freeling_wrapper import PoS, init_freeling


def server(args):
    print("A iniciar o servidor...")
    tk, sp, morfo, tagger, sense, wsd, parser = init_freeling("pt")
    if len(args) < 2:
        host = 'localhost'
        port = 1234
    else:
        host = args[1]
        port = int(args[2])
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(10)

    print("Servidor pronto.")

    while True:
        conn, addr = sock.accept()
        print("Ligado:", str(addr))
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print("Recebi:", str(data))
            pos = PoS(str(data), tk, sp, morfo, tagger, sense, wsd, parser)
            print("Enviei:", pos)
            conn.send(pickle.dumps(pos))
        conn.close()


def main(argv):
    p1 = mp.Process(target=server, args=(argv,))
    p1.start()

    while True:
        cmd = input()
        if cmd == "sair":
            p1.terminate()
            break

if __name__ == '__main__':
    main(sys.argv)