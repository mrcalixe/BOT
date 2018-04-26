#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, json, Actions
from aux_functions import *
from Machine_Learning.ml import *
from FreeLing_Client.freeling_client import Client
from DB import DB_Keywords, DB_Frases, Users_DB, readback_users, readback_frases_keywords, dump_frases_keywords, \
    dump_users

current_user = "Utilizador"  # type: str
bot_name = "Bot"             # type: str


users_db = None
frases_db = DB_Frases()
keywords_db = DB_Keywords()
#known_db = None

sock = None


def init_dbs():
    global frases_db
    global keywords_db
    global know_db
    global users_db
    global current_user
    users_db = Users_DB()
    try:
        users_db = readback_users("users_db.json")
        frases_db, keywords_db = readback_frases_keywords("frases_keywords_train.json")
    except AttributeError and FileNotFoundError and json.decoder.JSONDecodeError:
        pass



def main(args):
    global frases_db
    global keywords_db
    global know_db
    global users_db
    global current_user
    global sock
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
                    #Adicionar frase ao estado do utilizador
                    print(bot_name,':',f(s))
        except EOFError and KeyboardInterrupt:
            pass
    except ValueError:
        pass
    finally:
        dump_frases_keywords(frases_db, keywords_db, 'frases_keywords_db.json')
        dump_users(users_db, "users_db.json")
        sock.close()



def first_conversation():
    # Perguntar se quer continuar anonimo ou com utilizador normal
    global current_user
    n = input("Introduza o seu nome, ou prima ENTER para continuar anónimo:\nNome: ")
    if n != "":
        if Users_DB.check_user(n):
            print("Bem-vindo de volta "+ n +".")
        else:
            print("Bem-vindo "+ n +", eu sou um Bot :)")
        current_user = n
    else:
        users_db.add_user(n)
        print("Bem-vindo, eu sou um Bot :)")


def call_func(func, args):
    return getattr(Actions, func)(dict=args)


def f(s):
    global sock

    tagged = parse_analise(sock.PoS(s))

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