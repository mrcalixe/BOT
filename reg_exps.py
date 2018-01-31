#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re


#TODO Modelar as expressões regulares
'''
Existe um dicionário que contém 
'''


Regexs = {}

qualquer_coisa       = re.compile('.*')
nome_proprio_geral   = re.compile('NP*')
pergunta             = re.compile('Fit')
verbo_indicativo_presente_geral = re.compile('VMIP*')
adverbio_geral       = re.compile('RG')

verbos_lugar = re.compile('(ficar|estar|situar|localizar)')

Regexs['pergunta_lugar'] = {'exp' : [(qualquer_coisa, adverbio_geral),
                                     (verbos_lugar,verbo_indicativo_presente_geral),
                                     (qualquer_coisa, nome_proprio_geral),
                                     (qualquer_coisa, pergunta)]}


#TODO definir regras onde se consiga ultrapassar o facto de poder utilizar nomes comuns, pronomes, determinantes e preposições no meio da frase
# Por exemplo: Onde fica Braga = Onde se situa a cidade de Braga


def match(frase_tagged):
    for key in Regexs.keys():
        print("A testar", key)
        teste = True
        i = 0
        exp = (Regexs[key])['exp']
        while teste and i < len(frase_tagged):
            if exp[i][1].match(frase_tagged[i][1]):
                teste = teste and True
            else:
                teste = teste and False
            i += 1
        if teste:
            return key


def get_nome(tagged):
    for (palavra, tag) in tagged:
        if nome_proprio_geral.match(tag):
            return palavra
    raise ValueError('Não existe nenhum nome próprio na frase.')