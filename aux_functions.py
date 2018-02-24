#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random, json
import sqlite3 as sql

def oneOf(arr):
    # Simples função que escolhe aleatóriamente um elemento de um array
    rand_idx = random.randint(0,len(arr) - 1)
    return arr[rand_idx]

class State:
    # Futura classe que representará o estado do BOT
    def __init__(self):
        self.sys = 1

class Knowledge_BD:
    # Esta BD tem o conhecimento que o BOT adquiriu (numa parte inicial, só sobre música)
    def __init__(self, tables = False):
        self.db = sql.connect('Knowledge_DB/db')
        self.id = 0
        if tables:
            cursor = self.db.cursor()
            cursor.execute('''
                CREATE TABLE music(id INTEGER PRIMARY KEY,\
                                   author TEXT,
                                   band TEXT,
                                   year INTEGER,
                                   music TEXT)
                                ''')
            self.db.commit()
            cursor.close()

    # Esta função insere na base de dados informação sobre o conhecimento de um autor, ou música
    def insert_knowledge(self, author, band, year, music):
        cursor = self.db.cursor()
        cursor.execute('''
            INSERT INTO music(id, author, band, year, music)
            VALUES (?,?,?,?,?), (self.id, author, band, year, music)''')
        self.db.commit()
        cursor.close()

    # Esta função vai à base de dados buscar informação sobre um autor
    def get_by_author(self, author):
        cursor = self.db.cursor()
        cursor.execute('''
            SELECT * FROM music
              WHERE author = ?''', author)
        all_rows = self.cursor.fetchall()
        cursor.close()
        return all_rows


class Users_DB:
    # Dicionário que contém os utilizadores que já utilizaram o BOT
    def __init__(self):
        self.users = {}
        self.users.clear()

    # Visto que não existe a função has_key no dicionário, basta tentar aceder à chave e caso haja uma exceção significa que não existe entrada
    def check_user(self, user):
        try:
            t = self.users[user]
            return True
        except KeyError:
            return False

    # Adiciona uma entrada de um utilizador.
    # Nesta entrada ainda vai existir um log com as vezes que este utilizador já utilizou o BOT, bem como o tema das conversas.
    def add_user(self, user):
        self.users[user] = {}


# Esta função escreve num ficheiro em formato JSON o dicionário dos utilizadores
def dump_users(users_db, file):
    with open(file, "w+") as outfile:
        json.dump(users_db, outfile)

# Esta função lê de um ficheiro no formato JSON o dicionário dos utilizadores
def readback_users(file):
    with open(file, "r") as outfile:
        data = json.load(outfile)
    return data
