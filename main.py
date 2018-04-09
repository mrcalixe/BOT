#!/usr/bin/python3
# -*- coding: utf-8 -*-

from aux_functions import *
from Machine_Learning.ml import *
import sys
from freeling_client import Client
from DBs import DB as frase_keys_db
import Actions

know_db = None
users_db = None
current_user = "Utilizador"  # type: str
bot_name = "Bot"             # type: str


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
        users_db.users = readback_users("DBs/users_db.json")
        frases, keywords = frase_keys_db.readback("DBs/frases_keywords_train.json")
        frases_db = frase_keys_db.DB_Frases(frases)
        keywords_db = frase_keys_db.DB_Keywords(keywords)
    except AttributeError and FileNotFoundError and json.decoder.JSONDecodeError:
        pass



def main(args):
    global frases_db
    global keywords_db
    global know_db
    global users_db
    global current_user
    if len(args) == 1:
        host = 'localhost'
        port = 1234
    else:
        host = args[1]
        port = int(args[2])

    sock = Client(host, port)

    init_dbs()

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
        frase_keys_db.dump(frases_db, keywords_db, 'DBs/frases_keywords_db.json')
        dump_users(users_db.users, "DBs/users_db.json")
        sock.close()



def first_conversation():
    # Perguntar se quer continuar anonimo ou com utilizador normal

    n = input("Introduza o seu nome, ou prima ENTER para continuar anónimo:\n    Nome: ")
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


def call_func(func, args):
    return getattr(Actions, func)(dict=args)


def f(s, sock):
    sock.send(s)
    tagged = parse_analise(sock.recv())

    res = verifica(tagged)
    print("Expressões:", res)

    if res != {}:
        key = random.choice(list(res.keys()))
        return call_func(Regexs[key]['action'], res[key])
    else:
        res_esp = verifica_especiais(tagged)
        print("Expressões_Especiais:", res_esp)

        if res_esp != {}:
            key = random.choice(list(res_esp.keys()))
            return call_func(Regexs_Especiais[key]['action'], res_esp[key])
        else:
            res_back = verifica_backup(tagged)
            print("Expressões_backup:", res_back)

            if res_back != {}:
                key = random.choice(list(res_back.keys()))
                return call_func(Regexs_Backup[key]['action'], res_back[key])
            else:
                return 'Não consegui entender...'

if __name__ == '__main__':
    main(sys.argv)