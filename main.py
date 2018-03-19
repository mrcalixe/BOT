#!/usr/bin/python3
# -*- coding: utf-8 -*-

from aux_functions import *
from reg_exps import *
from ml import *
from wikipedia_wrapper import *
import socket, sys, pickle
from freeling_client import Client

know_db = None
users_db = None
current_user = "Anónimo"
bot_name = "Bot"


#TODO alterar a forma como o BOT inicia ao perguntar o nome.
#TODO Questionar antes se quer continuar como anonimo.


def main(args):
    if len(args) == 1:
        host = 'localhost'
        port = 1234
    else:
        host = args[1]
        port = int(args[2])

    sock = Client(host, port)

    try:
        global know_db
        global users_db
        global current_user
        know_db = Knowledge_BD(tables=False)
        users_db = Users_DB()
        try:
            users_db.users = readback_users("users_db.json")
        except AttributeError and FileNotFoundError and json.decoder.JSONDecodeError:
            pass

        first_conversation()

        try:
            while True:
                s = input(current_user+": ")
                if s == "sair":
                    break
                else:
                    print(bot_name,':',f(s, sock))
        except EOFError and KeyboardInterrupt:
            pass
    except ValueError:
        pass
    finally:
        know_db.db.close()
        dump_users(users_db.users, "users_db.json")
        sock.close()



def first_conversation():
    # Ask user name
    print("Olá! Qual é o seu nome?")
    try:
        n = input()
        if users_db.check_user(n):
            print("Bem-vindo de volta", n+".")
        else:
            users_db.add_user(n)
            print("Bem-vindo, eu sou um Bot :)")

        global current_user
        current_user = n
    except:
        raise ValueError("Erro na função \"input\"")



def f(s, sock):
    sock.send(s)
    tagged = sock.recv()
    parsed = parse_freeling_analise(tagged)

    res = match(parsed)
    print("Expressões:", res)
    if res != []:
        a = feature(res)
        return a
    else:
        return 'Não consegui entender.'

if __name__ == '__main__':
    main(sys.argv)