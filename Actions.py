from Wrappers.wikipedia_wrapper import procura_nome
from Wrappers.google_maps_wrapper import procura_lugar


class Actions:
    def __init__(self):
        self.lista = []

    def pergunta_nome(self, nome, *args):
        return procura_nome(nome)

    def pergunta_pessoa(self, nome, *args):
        return procura_nome(nome)

    def procura_lugar(self, lugar, *args):
        procura_lugar(lugar)

    def bem_vindo(self, interjeicao, *args):
        return 'Olá :)'

    def adeus(self, interjeicao, *args):
        return 'Até uma próxima :)'

Act = Actions()