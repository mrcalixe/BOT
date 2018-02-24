class Artigos:
    definidos = ['o', 'os', 'a', 'as']
    indefinidos = ['um', 'uns', 'uma', 'umas']

    def __eq__(self, other):
        other = other.lower()
        if other in self.definidos or self.indefinidos:
            return True
        else:
            return False


Pronomes_Pessoais = {'Singular' : {'primeira_pessoa' : ['eu'],
                                   'segunda_pessoa'  : ['tu'],
                                   'terceira_pessoa' : ['ele', 'ela']},
                     'Plurar'   : {'primeira_pessoa' : ['nós'],
                                   'segunda_pessoa'  : ['vós'],
                                   'terceira_pessoa' : ['eles', 'elas']}
                     }


Pronomes_Possessivos = {'Singular' : {'primeira_pessoa' : ['meu', 'minha', 'nosso', 'nossa'],
                                      'segunda_pessoa'  : ['teu', 'tua', 'vosso', 'vossa'],
                                      'terceira_pessoa' : ['seu', 'sua', 'dele', 'dela']},
                        'Plural'   : {'primeira_pessoa' : ['meus', 'minhas', 'nossos', 'nossas'],
                                      'segunda_pessoa'  : ['teus', 'tuas', 'vossos', 'vossas'],
                                      'terceira_pessoa' : ['seus', 'suas', 'deles', 'delas']}
                        }


class Adverbios:
    afirmacao = ['sim', 'perfeitamente', 'pois sim', 'positivamente', 'efetivamente', 'certamente']
    negacao = ['não', 'nunca', 'nada', 'jamais']
    modo = ['bem', 'mal', 'melhor', 'pior', 'certo', 'também', 'depressa', 'devagar']
    lugar = ['aqui', 'ali', 'lá', 'além', 'perto', 'longe', 'fora', 'dentro', 'onde', 'acima', 'adiante']
    duvida = ['talvez', 'porventura', 'provavelmente']
    intensidade = ['muito', 'pouco', 'bastante', 'menos', 'mais', 'tão', 'tanto', 'todo', 'completamente', 'excessivamente']
    tempo = ['agora', 'já', 'logo', 'cedo', 'tarde', 'antes', 'depois', 'sempre', 'nunca', 'jamais', 'hoje', 'ontem', 'amanhã']
    interrogativos = ['onde', 'quando', 'como', 'por que']
    inclusao = ['até', 'também']
    exclusao = ['exclusivamente', 'somente']

class Preposicoes:
    essenciais = ['a', 'ante', 'até', 'após', 'de', 'desde', 'em', 'entre', 'com', 'contra', 'para', 'por', 'perante', 'sem', 'sobe', 'sob']
