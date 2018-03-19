import json


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

    def __init__(self):
        self.db = {}

    def check_key(self, key):
        try:
            self.db[key]
            return True
        except KeyError:
            return False

    def add(self, key, action, keywords):
        self.db[key] = {'action': action, 'keywords': keywords}

    def update(self, key, action=None, keywords=None):
        if action:
            self.db[key]['action'] = action
        if keywords:
            self.db[key]['keywords'] = keywords

    def dump(self, file):
        '''Escreve num ficheiro em formato JSON'''
        with open(file, "w+") as outfile:
            json.dump(self.db, outfile)

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

    def __init__(self):
        self.db = {}

    def check_key(self, key):
        try:
            self.db[key]
            return True
        except KeyError:
            return False

    def add(self, key, lista):
        self.db[key] = lista

    def update(self, key, lista=None):
        if lista:
            self.db[key] = lista

    def dump(self, file):
        '''Escreve num ficheiro em formato JSON'''
        with open(file, "w+") as outfile:
            json.dump(self.db, outfile)

    def readback(self, file):
        '''Lê de um ficheiro no formato JSON'''
        with open(file, "r") as outfile:
            self.db = json.load(outfile)


def dump(DB_frases, DB_Keywords, file):
    with open(file, "w+") as outfile:
        json.dump({"treino": DB_frases, "keywords": DB_Keywords}, outfile)


def readback(file):
    with open(file, "r") as outfile:
        Tmp = json.load(outfile)
        return Tmp["treino"], Tmp["keywords"]
