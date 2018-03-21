#!/usr/bin/python3
# -*- coding: utf-8 -*-

from aux_functions import *
from reg_exps import *
from ml import *
from wikipedia_wrapper import *
import sys
from freeling_client import Client
import DB as frase_keys_db

know_db = None
users_db = None
current_user = "Anónimo"
bot_name = "Bot"


#TODO alterar a forma como o BOT inicia ao perguntar o nome.
#TODO Questionar antes se quer continuar como anonimo.


frases_db = None
keywords_db = None


def init_dbs():
    global frases_db
    global keywords_db
    global know_db
    global users_db
    global current_user
    know_db = Knowledge_BD(tables=False)
    users_db = Users_DB()
    try:
        users_db.users = readback_users("users_db.json")
        frases, keywords = frase_keys_db.readback("frases_keywords_train.json")
        frases_db = frase_keys_db.DB_Frases(frases)
        keywords_db = frase_keys_db.DB_Keywords(keywords)
    except AttributeError and FileNotFoundError and json.decoder.JSONDecodeError:
        pass



def main(args):
    if len(args) == 1:
        host = 'localhost'
        port = 1234
    else:
        host = args[1]
        port = int(args[2])

    sock = Client(host, port)

    try:
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
    # Perguntar se quer continuar anonimo ou com utilizador normal

    n = input("Introduza o seu nome, ou para como utilizador anónimo basta deixar em branco (carregar só na tecla ENTER)")
    if n != "":
        try:
            print("Bem-vindo de volta", n+".")
            global current_user
            current_user = n
        except:
            raise ValueError("Erro na função \"input\"")
    else:
        users_db.add_user(n)
        print("Bem-vindo, eu sou um Bot :)")



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