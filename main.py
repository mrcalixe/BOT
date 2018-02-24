#!/usr/bin/python3
# -*- coding: utf-8 -*-

from aux_functions import *
from reg_exps import *
from ml import *
from web_search import *


know_db = None
users_db = None
current_user = "Anónimo"
bot_name = "Bot"


def main():
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
                elif s == 'admin':
                    print('|-- Admin mode on --|')
                    while True:
                        s = input("$ ")
                        if s=='sair':
                            print('|-- Admin mode off --|')
                            break
                        else:
                            print(PoS(s))
                else:
                    print(bot_name,':',f(s))
        except EOFError and KeyboardInterrupt:
            pass
    except ValueError:
        pass
    finally:
        know_db.db.close()
        dump_users(users_db.users, "users_db.json")



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



def f(s):
    tagged = PoS(s)
    parsed = parse_freeling_analise(tagged)
    res = match(parsed)
    if res != []:
        a = PoS_feature(res)
    else:
        return 'Não consegui entender.'
    '''
    if res == 'pergunta_lugar':
        nome = get_nome(tagged)
        return procura_lugar(nome)
    else:
        return 'Desculpa, ainda não sou capaz de processar esse tipo de questões :P'
    '''

main()