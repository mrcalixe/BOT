# -*- coding: utf-8 -*-

import nltk
from nltk.corpus import treebank
from aux_functions import *

know_db = None
users_db = None
bot_name = ["Qualquer coisa :)", "Tenta adivinhar ;)", "Eu não me chamo nada, mas chamam-me de bot :P)"]


def first_conversation():
    return 1


def main():
    global know_db
    global users_db
    know_db = Knowledge_BD(tables=True)
    users_db = Users_DB()
    while True:
        try:
            s = input('Tu: ')
        except EOFError:
            break

main()
