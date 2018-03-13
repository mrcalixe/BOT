from wikipedia_wrapper import procura_nome
from google_maps_wrapper import procura_lugar


class Actions:
    def __init__(self):
        self.lista = []

    def pergunta_pessoa(self, nome):
        return procura_nome(nome)

    def procura_lugar(self, lugar):
        procura_lugar(lugar)


def call_func(a, func):
    method = getattr(a, func)