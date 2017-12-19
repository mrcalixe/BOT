#!/usr/bin/python3
# -*- coding: utf-8 -*-

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import floresta
from aux_functions import *
from reg_exps import *


know_db = None
users_db = None
current_user = "Unknown"
bot_name = ["Qualquer coisa :)", "Tenta adivinhar ;)"]


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
                else: print(f(s))
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
            print("Bem-vindo, caso não saiba ou não tenha reparado eu sou um Bot :)")

        global current_user
        current_user = n
    except:
        raise ValueError("Erro na função \"input\"")




def f(s):
    if len(s) <= 0:
        return 'Erro em s'
    m = regex_asking_who_sings.match(s)
    if m:
        return 'Match 1'
    m = regex_asking_who_sings2.match(s)
    if m:
        return 'Match 2'
    m = regex_artist_search.match(s)
    if m:
        return 'Match 3'

    return 'Desculpa, ainda não sou capaz de processar esse tipo de questões :P'

main()