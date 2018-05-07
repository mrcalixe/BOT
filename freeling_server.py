#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, socket, json, pickle
import multiprocessing as mp
from Wrappers.freeling_wrapper import init_freeling, PoS
import Configurations as Conf


global tk, sp, morfo, tagger, sense, wsd, parser
global sock


def server():
    global tk, sp, morfo, tagger, sense, wsd, parser
    global sock

    while True:
        conn, addr = sock.accept()
        print("\nDEBUG:Ligado:", str(addr))
        while True:
            data = conn.recv(1024)
            if not data:
                break

            loaded = pickle.loads(data)
            print("\nDEBUG:Recebi:", str(data))
            send = None
            if 'pos' in loaded.keys():
                send = PoS(loaded['pos'], tk, sp, morfo, tagger, sense, wsd, parser)

            elif 'token' in loaded.keys():
                send = str(tk.tokenize(loaded['token']))

            elif 'split' in loaded.keys():
                send = tk.tokenize(loaded['split'])
                send = sp.split(send)

            print("\nDEBUG:A enviar:", send)
            conn.send(pickle.dumps(send))
        conn.close()


# Protocolo
# {'pos' : frase} <- fazer a analise PoS
# {'token' : frase} <- fazer o tokenize
# {'split' : frase} <- fazer o split


def main(args):
    global tk, sp, morfo, tagger, sense, wsd, parser
    global sock

    print("DEBUG:A iniciar o servidor FreeLing...")
    tk, sp, morfo, tagger, sense, wsd, parser = init_freeling("pt")
    if len(args) < 2:
        host = Conf.default_ip
        port = Conf.default_port
    else:
        host = args[1]
        port = int(args[2])
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(10)

    print("DEBUG:Servidor pronto.")

    p1 = mp.Process(target=server)
    p1.start()

    while True:
        cmd = input("admin@freeling_server:~/$ ")
        if cmd == "sair":
            p1.terminate()
            break
        elif cmd == "":
            pass
        else:
            print(PoS(cmd, tk, sp, morfo, tagger, sense, wsd, parser))

if __name__ == '__main__':
    main(sys.argv)