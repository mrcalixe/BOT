#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, json, Actions
from aux_functions import *
from Machine_Learning.ml import *
import FreeLing_Client.freeling_client as freeling
from DB import DB_Keywords, DB_Frases, Users_DB, readback_users, readback_frases_keywords, dump_frases_keywords, \
    dump_users

import Configurations as Conf

current_user = Conf.default_user
bot_name = Conf.bot_name



users_db = None
frases_db = DB_Frases()
keywords_db = DB_Keywords()


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



def first_conversation():
    # Perguntar se quer continuar anonimo ou com utilizador normal
    global current_user
    global users_db
    n = input("Introduza o seu nome, ou prima ENTER para continuar anónimo:\nNome: ")
    if n != "":
        if users_db.check_user(n):
            print("Check user True")
            print("Bem-vindo de volta "+ n +".")
        else:
            print("Check user False")
            print("Bem-vindo "+ n +", eu sou um Bot :)")
            users_db.add_user(n)
        current_user = n
    else:
        users_db.add_user(n)
        print("Bem-vindo, eu sou um Bot :)")


def call_func(func, args):
    return getattr(Actions, func)(dict=args)


def substitui_por_originais(res, tagged, frase):
    for key in res:
        d = res[key]
        for k in d:
            v = d[k]
            for (lemma, tag, word) in tagged:
                if v == lemma:
                    print("SPO:A substituir", lemma, "por", word)
                    d[k] = word
        res[key] = d
    return res


def f(s):
    # Mudado para o novo modelo
    analyzed = freeling.analyse(s)
    dot, tagged = freeling.extract(analyzed['sentences'][0])
    parsed_tag = parse_analise(tagged)

    #TODO falta a parte da verificação e ação
    #TODO implementar um classificador para escolher ações do que foi analisado

    res = verifica(parsed_tag)
    print("Expressões:", res)

    if res != {}:
        key = random.choice(list(res.keys()))
        res = substitui_por_originais(res, tagged, s)
        return call_func(Regexs[key]['action'], res[key])
    else:
        res_esp = verifica_especiais(parsed_tag)
        print("Expressões_Especiais:", res_esp)

        if res_esp != {}:
            key = random.choice(list(res_esp.keys()))
            res = substitui_por_originais(res, tagged, s)
            return call_func(Regexs_Especiais[key]['action'], res_esp[key])
        else:
            res_back = verifica_backup(parsed_tag)
            res = substitui_por_originais(res, tagged, s)
            print("Expressões_backup:", res_back)

            if res_back != {}:
                key = random.choice(list(res_back.keys()))
                res = substitui_por_originais(res, tagged, s)
                return call_func(Regexs_Backup[key]['action'], res_back[key])
            else:
                return 'Não consegui entender...'

if __name__ == '__main__':
    main(sys.argv)