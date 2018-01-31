"""O estudo das formas da linguagem, isto é, das formas que as palavras podem tomar, chama-se morfologia.
Muitas palavras mudam de forma, enquanto outras não se modificam.
As que mudam de forma são variáveis ou flexivas.
As que não mudam de forma são invariáveis ou inflexivas."""


class Variaveis:
    def __str__(self):
        return 'Palavras variáveis são aquelas que mudam de forma.'


class Invariaveis:
    def __str__(self):
        return 'Palavras invariáveis são aquelas que não mudam de forma.'


class Substantivos(Variaveis):
    def __str__(self):
        return 'Os nomes substantivos, ou simplesmente substantivos, são nomes de:\n' \
               'Pessoas, Animais, Coisas, Qualidades, Estados e Atos ou ações'

    class Proprios:
        def __str__(self):
            return 'Os nomes que servem para designar particularmente uma determinada pessoa, ' \
                   'coisa ou animal, chamam-se substantivos próprios.'
        def check(self, nome):
            # Testar se todas as outras letras são minúsculas
            teste = True
            for i in range(1,len(nome)):
                teste = teste and nome[i].islower()
            #Verificar se a 1ª é maiuscula e as outras minusculas
            if not nome[0].islower and teste:
                return True
            else:
                return False

    class Coletivos:
        def __str__(self):
            return 'As palavras que significam uma colecção, ou um certo número de coisas de uma espécie, ' \
                   'um agregado ou conjunto de pessoas ou de animais, chamam-se substantivos colectivos.'


class Adjetivos(Variaveis):
    def __str__(self):
        return 'Adjetivos são palabras cuja significação se junta à dos substantivos' \
               ' para os qualificar ou para indicar os estados das pessoas, coisas ou dos animais' \
               ' significados por substantivos.'


class Numerais(Variaveis):
    def __str__(self):
        return 'As palavras que indicam o número de pessoas, de coisas ou de animais, chamam-se numerais cardinais.\n' \
               'As palavras que indicam o lugar ocupado pelas pessoas, pelas coisas ou pelos animais, ' \
               'numa série ou ordem, chamam-se numerais ordinais\n' \
               'As palavras que indicam que um certo número de pessoas, de coisas ou de animais ' \
               'se multiplicou por outro número, chamam-se numerais proporcionais e também numerais multiplicativos:\n' \
               'Os nomes que designam coleção de pessoas, de coisas e de animais, chamam-se numerais colectivos'

    class Cardinais:
        cardinais = {0 : ('unidade', {0    : 'zero',
                                      1    : 'um',
                                      2    : 'dois',
                                      3    : 'três',
                                      4    : 'quatro',
                                      5    : 'cinco',
                                      6    : 'seis',
                                      7    : 'sete',
                                      8    : 'oito',
                                      9    : 'nove'}),
                     1 : ('dezena', {10   : 'dez',
                                     11   : 'onze',
                                     12   : 'doze',
                                     13   : 'treze',
                                     14   : 'catorze',
                                     15   : 'quinze',
                                     16   : 'dezasseis',
                                     17   : 'dezassete',
                                     18   : 'dezoite',
                                     19   : 'dezanove',
                                     20   : 'vinte',
                                     30   : 'trinta',
                                     40   : 'quarenta',
                                     50   : 'cinquenta',
                                     60   : 'sessenta',
                                     70   : 'setenta',
                                     80   : 'oitenta',
                                     90   : 'noventa'}),
                     2 : ('centena', {100  : 'cem',
                                      200  : 'duzentos',
                                      300  : 'trezentos',
                                      400  : 'quatrocentos',
                                      500  : 'quinhentos',
                                      600  : 'seiscentos',
                                      700  : 'setecentos',
                                      800  : 'oitocentos',
                                      900  : 'novecentos'}),
                     3 : ('milhar', {1000 : 'mil'})}

        def to_cardinal(self, numero):
            a = list(str(numero))
            s = ''
            for i in range(len(a)):
                s = 'a'


class Pronomes(Variaveis):
    def __str__(self):
        return 'As palavras que substituem os nomes, isto é, que simplesmente indicam as pessoas, as coisas ou os animais, ' \
               'e que, por isso, fazem as vezes dos nomes substantivos ou adjectivos, chamam-se pronomes.'


class Artigos(Variaveis):
    def __str__(self):
        return 'Os pronomes demonstrativos o, a, os e as, quando estão colocados antes dos substantivos e mostram ' \
               'que nos referimos a determinada pessoa, determinada coisa ou determinado animal, tomam o nome de artigos definidos:\n' \
               'Os pronomes indefinidos um, uma, uns e umas, quando estão colocados antes de substantivos ' \
               'e mostram que nos referimos a uma pessoa, a uma coisa ou a um animal indeterminado, tomam o nome de artigos indefinidos.'


class Verbos(Variaveis):
    """
    Nesta classe, definimos cada classe de conjugação dos tempos verbais.
    Existe o singular e o plurar, onde dentro de cada uma existe um Mapa com as pessoas a conjugar,
    bem como o sufixo que o verbo deve assumir, e ainda tem o número de letras a remover para poder concatenar o sufixo.
    """

    def __str__(self):
        return 'As palavras com que afirmamos a existência, uma acção, um estado ou uma qualidade ' \
               'que atribuímos a uma pessoa, a uma coisa ou a um animal chamam-se verbos.'


    class Presente:
        class Singular:
            pessoas = {'primeira': ['o', 2],
                       'segunda': ['s', 1],
                       'terceira': ['', 1]}
        class Plural:
            pessoas = {'primeira': ['mos', 1],
                       'segunda': ['is', 1],
                       'terceira': ['m', 1]}


    class Preterito_Perfeito:
        """
        Na conjugação deste tempo, nomeadamente nos verbos de 2ª conjugação, existe um caso especial.
        """
        class Singular:
            def __init__(self, verbo):
                conj = self.conjugacao(verbo)
                if conj == 1:
                    if verbo[:len(verbo) -2][-1] in ['q', 'g']:
                        self.pessoas = {'primeira': ['uei', 2],
                                   'segunda': ['ste', 1],
                                   'terceira': ['ou', 2]}
                    else:
                        self.pessoas = {'primeira' : ['ei', 2],
                                   'segunda'  : ['ste', 1],
                                   'terceira' : ['ou', 2]}
                else:
                    self.pessoas = {'primeira': ['i', 2],
                               'segunda': ['stes', 1],
                               'terceira': ['ram', 1]}

        class Plural:
            pessoas = {'primeira': ['mos', 1],
                       'segunda' : ['stes', 1],
                       'terceira': ['ram', 1]}

    class Infinitivo_Pessoal:
        class Singular:
            pessoas = {'primeira': ['o', 2],
                       'segunda': ['s', 1],
                       'terceira': ['', 1]}
        class Plural:
            pessoas = {'primeira': ['mos', 1],
                       'segunda': ['is', 1],
                       'terceira': ['m', 1]}


    def conjugacao(self, verbo):
        if verbo[-2:len(verbo)].lower() == 'ar':
            return 1
        if verbo[-2:len(verbo)].lower() == 'er':
            return 2
        elif verbo[-2:len(verbo)].lower() == 'ir':
            return 3
        else:
            raise ValueError('Não é um verbo')


    def conjuga_aux(self, verbo, singular, plural):
        c = []
        size = len(verbo)

        v = singular.pessoas['primeira']
        conj = verbo[:size - v[-1]] + v[0]
        c.append(conj)

        v = singular.pessoas['segunda']
        conj = verbo[:size - v[-1]] + v[0]
        c.append(conj)

        v = singular.pessoas['terceira']
        conj = verbo[:size - v[-1]] + v[0]
        c.append(conj)

        v = plural.pessoas['primeira']
        conj = verbo[:size - v[-1]] + v[0]
        c.append(conj)

        v = plural.pessoas['segunda']
        conj = verbo[:size - v[-1]] + v[0]
        c.append(conj)

        v = plural.pessoas['terceira']
        conj = verbo[:size - v[-1]] + v[0]
        c.append(conj)

        return c


    def conjuga(self, verbo, tempo):
        v = Verbos()
        if tempo is Verbos.Presente:
            sing = v.Presente.Singular()
            plu = v.Presente.Plural()
            return self.conjuga_aux(verbo, sing, plu)
        elif tempo is Verbos.Preterito_Perfeito:
            sing = v.Preterito_Perfeito.Singular(verbo)
            plu = v.Preterito_Perfeito.Plural()
            return self.conjuga_aux(verbo, sing, plu)
        elif tempo is Verbos.Infinitivo_Pessoal:
            sing = v.Infinitivo_Pessoal.Singular()
            plu = v.Infinitivo_Pessoal.Plural()
            return self.conjuga_aux(verbo, sing, plu)


class Adverbios(Invariaveis):
    def __str__(self):
        return 'Há certas palavras que servem para modificar a significação dos verbos, dos adjectivos e de outros advérbios. ' \
               'Essas palavras chamam-se, em gramática, advérbios.'

class Preposicoes(Invariaveis):
    def __str__(self):
        return 'As partículas ou palavras inflexivas que estabelecem a relação entre duas palavras' \
               ' ou entre duas partes de uma oração chamam-se preposições.'

class Conjuncoes(Invariaveis):
    def __str__(self):
        return 'As palavras inflexivas que ligam duas partes da oração ' \
               'ou ligam entre si orações ou proposições chamam-se, em gramática, conjunções.'

class Interjeicoes(Invariaveis):
    def __str__(self):
        return 'Nas expressões seguintes encontram-se as partículas ai! ui! ah! e oh!, ' \
               'com as quais se exprimem sentimentos vários e às quais se dá o nome de interjeições.'