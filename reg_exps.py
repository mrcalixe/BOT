#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re


#TODO Modelar as expressões regulares
'''
Existe um dicionário que contém 
'''


Regexs = {}


#Nomes
nome_geral                      = re.compile('N*')
nome_proprio_geral              = re.compile('NP*')
nome_comum_geral                = re.compile('NC*')


#Verbos
verbo_geral                     = re.compile('V*')
verbo_indicativo_presente_geral = re.compile('VMIP*')


#Advérbios
adverbio_geral                  = re.compile('RG')


#Pronomes
pronome_geral                   = re.compile('P*')
pronome_pessoal_geral           = re.compile('PP*')


#Determinantes
determinante_geral              = re.compile('D*')
determinante_artigo_geral       = re.compile('DA*')


#Pontuação
pergunta                        = re.compile('Fit')


#Expressões gerais
qualquer_coisa                  = re.compile('.*')

verbos_lugar = re.compile('(ficar|estar|situar|localizar)')


Regexs['pergunta_lugar'] = {'exp' : [
                                (qualquer_coisa, adverbio_geral),
                                ('relax', pronome_pessoal_geral),
                                (verbos_lugar,verbo_indicativo_presente_geral),
                                ('relax', determinante_geral),
                                (qualquer_coisa, nome_proprio_geral),
                                (qualquer_coisa, pergunta)
                                ]}



#TODO definir regras onde se consiga ultrapassar o facto de poder utilizar nomes comuns, pronomes, determinantes e preposições no meio da frase.
# Ou seja, relaxar a expressão regular para aceitar certo tipo de palavras antes e/ou depois dde outro tipo de palavras.
# Por exemplo: Onde fica Braga = Onde se situa a cidade de Braga




#TODO modelar o significado das preposições
# ligam dois termos da frase (palavras ou sintagmas), indicando diversas relações semânticas, desde movimento, a espaço ou tempo, entre outros.
# Ou seja, sempre que encontramos uma preposição, sabemos que os termos que antecede e sucede estão ligados e têm uma relação




#TODO modelar um estado de sistema. Guardar os objetos usados no FreeLing.




#TODO modelar uma forma de dar sentido à interpretação feita.

#[('onde', 'RG'), ('se', 'PP3CN00'), ('situar', 'VMIP3S0'), ('o', 'DA0FS0'), ('cidade', 'NCFS000'), ('de', 'SP'), ('braga', 'NP00000'), ('?', 'Fit')]




def check_exp(frase, exp):
    i = 0
    while i < len(exp):
        (palavra, tag) = exp[i]
        (palavra2, tag2) = frase[i]
        if palavra.match(palavra2) and tag.match(tag2):
            i += 1
        elif palavra == 'relax' and tag.match(tag2):
            i += 1
        else:
            break
    return (i == len(exp))


def match(frase_tagged):
    # Testar todas as expressões
    selected_regexs = []
    for key in Regexs.keys():
        print("A testar", key)
        exp = (Regexs[key])['exp']
        if check_exp(frase_tagged, exp):
            selected_regexs.append(key)
    return selected_regexs


def get_nome(tagged):
    for (palavra, tag) in tagged:
        if nome_proprio_geral.match(tag):
            return palavra
    raise ValueError('Não existe nenhum nome próprio na frase.')