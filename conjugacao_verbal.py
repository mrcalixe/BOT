from lingua_portuguesa import *

class Verbos:

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
        class Singular:
            def __init__(self, verbo):
                conj = conjugacao(verbo)
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


def conjugacao(verbo):
    if verbo[-2:len(verbo)].lower() == 'ar':
        return 1
    if verbo[-2:len(verbo)].lower() == 'er':
        return 2
    elif verbo[-2:len(verbo)].lower() == 'ir':
        return 3
    else:
        raise ValueError('Não é um verbo')

pron = Pronomes_Pessoais()


def conjuga_aux(verbo, singular, plural):
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


def conjuga(verbo, tempo):
    v = Verbos()
    if tempo is Verbos.Presente:
        sing = v.Presente.Singular()
        plu = v.Presente.Plural()
        return conjuga_aux(verbo, sing, plu)
    elif tempo is Verbos.Preterito_Perfeito:
        sing = v.Preterito_Perfeito.Singular(verbo)
        plu = v.Preterito_Perfeito.Plural()
        return conjuga_aux(verbo, sing, plu)
    elif tempo is Verbos.Infinitivo_Pessoal:
        sing = v.Infinitivo_Pessoal.Singular()
        plu = v.Infinitivo_Pessoal.Plural()
        return conjuga_aux(verbo, sing, plu)

