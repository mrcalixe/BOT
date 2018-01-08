class Artigos:
    definidos = ['o', 'os', 'a', 'as']
    indefinidos = ['um', 'uns', 'uma', 'umas']

    def __eq__(self, other):
        other = other.lower()
        if other in self.definidos or self.indefinidos:
            return True
        else:
            return False


class Pronomes_Pessoais:
    class Singular:
        primeira_pessoa = ['eu']
        segunda_pessoa = ['tu']
        terceira_pessoa = ['ele', 'ela']

    class Plurar:
        primeira_pessoa = ['nós']
        segunda_pessoa = ['vós']
        terceira_pessoa = ['eles', 'elas']


class Pronomes_Possessivos:
    primeira_pessoa = ['meu', 'meus', 'minha', 'minhas', 'nosso', 'nossos', 'nossa', 'nossas']
    segunda_pessoa = ['teu', 'teus', 'tua', 'tuas', 'vosso', 'vossos', 'vossa', 'vossas']
    terceira_pessoa = ['seu', 'seus', 'sua', 'suas', 'dele', 'deles', 'dela', 'delas']


class Adverbios:
    afirmacao = ['sim', 'perfeitamente', 'pois sim', 'positivamente', 'efetivamente', 'certamente']
    negacao = ['não', 'nunca', 'nada', 'jamais']
    modo = ['bem', 'mal', 'melhor', 'pior', 'certo', 'também', 'depressa', 'devagar']
    lugar = ['aqui', 'ali', 'lá', 'além', 'perto', 'longe', 'fora', 'dentro', 'onde', 'acima', 'adiante']
    dúvida = ['talvez', 'porventura', 'provavelmente']
    intensidade = ['muito', 'pouco', 'bastante', 'menos', 'mais', 'tão', 'tanto', 'todo', 'completamente', 'excessivamente']
    tempo = ['agora', 'já', 'logo', 'cedo', 'tarde', 'antes', 'depois', 'sempre', 'nunca', 'jamais', 'hoje', 'ontem', 'amanhã']
    interrogativos = ['onde', 'quando', 'como', 'por que']
    inclusão = ['até', 'também']
    exclusão = ['exclusivamente', 'somente']

class Preposicoes:
    essenciais = ['a', 'ante', 'até', 'após', 'de', 'desde', 'em', 'entre', 'com', 'contra', 'para', 'por', 'perante', 'sem', 'sobe', 'sob']
