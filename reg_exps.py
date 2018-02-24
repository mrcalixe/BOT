#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re


#TODO Modelar as expressões regulares
'''
Existe um dicionário que contém 
'''


Regexs = {}


#Nomes
nome_geral                      = r'N\w*'
nome_proprio_geral              = r'NP\w*'
nome_comum_geral                = r'NC\w*'


#Verbos
verbo_geral                     = r'V\w*'
verbo_indicativo_presente_geral = r'VMIP\w*'


#Advérbios
adverbio_geral                  = r'RG'


#Pronomes
pronome_geral                   = r'P\w*'
pronome_pessoal_geral           = r'PP\w*'


#Determinantes
determinante_geral              = r'D\w*'
determinante_artigo_geral       = r'DA\w*'


#Pontuação
pergunta                        = r'Fit'


#Expressões gerais
qualquer_palavra                = r'\w+'
relax                           = r'relax'
verbos_lugar = (r'(ficar|estar|situar|localizar)')


Regexs['pergunta_lugar'] = {'exp' : [
                                (qualquer_palavra, adverbio_geral),
                                (relax, pronome_pessoal_geral),
                                (verbos_lugar,verbo_indicativo_presente_geral),
                                (relax, determinante_geral),
                                (qualquer_palavra, nome_proprio_geral),
                                ('?', pergunta)
                                ]}


def compile_regexs():
    global Regexs
    for regex in Regexs.keys():
        exp = Regexs[regex]['exp']
        s = r''
        for (word, type) in exp:
            if word == r'relax':
                aux = r'(' + type + r'\:' + qualquer_palavra + r'){0,1}\s*'
            else:
                aux = r'(' + type + r'\:' + word + r')\s*'
            s = s + aux
        Regexs[regex] = re.compile(s)
    return Regexs

def parse_freeling_analise(analise):
    s = r''
    for (word, tag) in analise:
        aux = tag + r':' + word + r' '
        s = s + aux
    return s[:(len(s))-1]




def match(frase):
    matched = []
    for reg_exp in Regexs.keys():
        res = Regexs[reg_exp].findall(frase)
        if res != []:
            matched += [reg_exp]
    return matched




Regexs = compile_regexs()




#TODO modelar um estado de sistema. Guardar os objetos usados no FreeLing.



#TODO modelar uma forma de dar sentido à interpretação feita.