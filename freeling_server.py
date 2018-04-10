#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, socket, json, pickle
import multiprocessing as mp
from Wrappers.freeling_wrapper import init_freeling, PoS


def server(args):
    print("A iniciar o servidor FreeLing...")
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
            data = conn.recv(1024)
            if not data:
                break

            loaded = pickle.loads(data)
            print("Recebi:", str(data))
            send = None
            if 'pos' in loaded.keys():
                send = PoS(loaded['pos'], tk, sp, morfo, tagger, sense, wsd, parser)

            elif 'token' in loaded.keys():
                send = str(tk.tokenize(loaded['token']))

            elif 'split' in loaded.keys():
                send = tk.tokenize(loaded['split'])
                send = sp.split(send)

            print("A enviar:", send)
            conn.send(pickle.dumps(send))
        conn.close()


# Protocolo
# {'pos' : frase} <- fazer a analise PoS
# {'token' : frase} <- fazer o tokenize
# {'split' : frase} <- fazer o split


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