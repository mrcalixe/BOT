import hashlib, json

class DB:
    def __init__(self):
        self.db = {}

    # Visto que não existe a função has_key no dicionário, basta tentar aceder à chave e caso haja uma exceção significa que não existe entrada
    def check_key(self, key):
        try:
            t = self.db[key]
            return True
        except KeyError:
            return False


    def add(self, key, tipo, classe):
        self.db[key] = {'tipo' : tipo, 'classe' : classe}


    def update(self, key, tipo=None, classe=None):
        if tipo:
            self.db[key]['tipo'] = tipo
        if classe:
            self.db[key]['classe'] = classe


    def dump(self, file):
        '''Escreve num ficheiro em formato JSON'''
        with open(file, "w+") as outfile:
            json.dump(self.db, outfile)


    def readback(self, file):
        '''Lê de um ficheiro no formato JSON'''
        with open(file, "r") as outfile:
            self.db = json.load(outfile)