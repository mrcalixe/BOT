#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json, pickle
from State import State


class DB_Frases:
    '''
      Nesta DB, vamos armazenar todo o conhecimento do BOT.
      Criei numa classe Python para utilizar Dicionários.
      Fica assim numa fase inicial só para testar,
       e mais tarde penso em migrar os dados e adpatar o código para uma BD.

      Dicionário composto por chave -> valor, onde:
        chave: são frases que foram analisadas (ou provenientes de um ficheiro)
            {"action" : "procura_pessoa", "keywords" : ["nome", verbo]}
        key: Dicionário
               "action" (ação usada para processar o pedido) -> função
               "keywords" (que keywords são relevantes e o tipo delas) -> keys
    '''

    def __init__(self, db = None):
        if db:
            self.db = db
        else:
            self.db = {}

    def check_key(self, key):
        try:
            r = self.db[key]
            return True
        except KeyError:
            return False

    def get(self, key):
        try:
            r = self.db[key]
            return r
        except KeyError:
            return None

    def get_by_keywords(self, keys):
        r = []
        for key in self.db:
            if keys in self.db[key]['keywords']:
                r.append(self.db[key])
        return r

    def add(self, key, action, keywords):
        self.db[key] = {'action': action, 'keywords': keywords}

    def update(self, key, action=None, keywords=None):
        if action:
            self.db[key]['action'] = action
        if keywords:
            self.db[key]['keywords'] = keywords

    def dump(self, file):
        '''Escreve num ficheiro em formato JSON'''
        json.dump(self.db, file, ensure_ascii=False)

    def readback(self, file):
        '''Lê de um ficheiro no formato JSON'''
        with open(file, "r") as outfile:
            self.db = json.load(outfile)


class DB_Keywords:
    '''
        Nesta BD armazenamos todas as Keywords importantes e o(s) tipo(s) que lhe são associados
        Isto com o sentido de, ao analisar uma frase e retirando as componentes principais, anotámos que tipo de palavra é.
        Assim, o Bot pode comparar com frases futuras se as mesmas palavras apareceram e obter uma resposta mais acertada.
    '''

    def __init__(self, db = None):
        if db:
            self.db = db
        else:
            self.db = {}

    def check_key(self, key):
        try:
            r = self.db[key]
            return True
        except KeyError:
            return False

    def get(self, key):
        try:
            r = self.db[key]
            return r
        except KeyError:
            return None

    def get_by_type(self, type):
        r = []
        for key in self.db:
            if self.db[key]['TYPE'] == type:
                r.append(self.db[key])
        return r

    def add(self, key, lista):
        self.db[key] = lista

    def update(self, key, lista=None):
        if lista:
            self.db[key] = lista

    def dump(self, file):
        '''Escreve num ficheiro em formato JSON'''
        json.dump(self.db, file, ensure_ascii=False)

    def readback(self, file):
        '''Lê de um ficheiro no formato JSON'''
        with open(file, "r") as outfile:
            self.db = json.load(outfile)


class Users_DB:
    # Dicionário que contém os utilizadores que já utilizaram o BOT
    def __init__(self):
        self.users = {}

    # Visto que não existe a função has_key no dicionário, basta tentar aceder à chave e caso haja uma exceção significa que não existe entrada
    def check_user(self, user):
        try:
            if self.users[user]:
                return True
            else:
                return True
        except KeyError:
            return False

    # Adiciona uma entrada de um utilizador.
    # Nesta entrada ainda vai existir um log com as vezes que este utilizador já utilizou o BOT, bem como o tema das conversas.
    def add_user(self, user):
        if self.check_user(user):
            pass
        else:
            self.users[user] = {'state': State()}

    def add_frase(self, user, frase):
        try:
            self.users[user]['state'].add(frase)
        except KeyError:
            raise ValueError("Não existe esse utilizador.")


# Esta função escreve num ficheiro em formato JSON o dicionário dos utilizadores
def dump_users(users_db, file):
    with open(file, "wb") as outfile:
        outfile.write(pickle.dumps(users_db))

# Esta função lê de um ficheiro no formato JSON o dicionário dos utilizadores
def readback_users(file):
    try:
        with open(file, "rb") as outfile:
            data = pickle.load(outfile)
        return data
    except FileNotFoundError:
        return Users_DB()

def dump_frases_keywords(DB_frases, DB_Keywords, file):
    with open(file, "w") as outfile:
        json.dump({'frases': DB_frases.db, 'keywords': DB_Keywords.db}, outfile, ensure_ascii=False)


def readback_frases_keywords(file):
    try:
        with open(file, "r") as outfile:
            Tmp = json.load(outfile, )
            return DB_Frases(Tmp["frases"]), DB_Keywords(Tmp["keywords"])
    except FileNotFoundError:
        return DB_Frases(), DB_Keywords()
