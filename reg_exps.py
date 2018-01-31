# -*- coding: utf-8 -*-


#TODO Modelar as expressões regulares
'''
1ª Tentavia - Criar uma string onde se mete as tags como expressão regular, ou seja,
    RegEx -> adposition:S ; verb:ficar: ; determiner:A ; noun_* ; punctuation:parenthesis:close
    Faz match -> Onde fica Braga?
    
    Ou seja, a RegEx é feita da seguinte forma:
        Começa com o PoS de cada palavra, seguindo-se do seu valor.
        Quando o PoS vem com _{+,*} é o mesmo significado do que nas RegEx normais,
      ou seja, 1 ou mais e 0 ou mais respetivamente.
        Quando vem, por exemplo, verb:estar: e sem nada à frente, quer dizer
      que pode ser qualquer conjugação dessee verbo.
'''


Regexs = {}


Regexs['pergunta_lugar'] = {'exp' : ['RG', ['VMI*','ficar'], 'NP*', 'Fit']}





def match_aux(regex, frase_tagged):
    return True


def match(frase_tagged):
    for key in Regexs.keys():
        if match_aux(Regexs[key], frase_tagged):
            return key