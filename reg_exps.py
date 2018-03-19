#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re


# TODO Modelar as expressões regulares


Regexs = {}


# Nomes
nome_geral = r'N\w+'
nome_proprio_geral = r'NP\w+'
nome_comum_geral = r'NC\w+'


# Verbos
verbo_geral = r'V\w*'
verbo_indicativo_presente_geral = r'VMIP\w*'


# Advérbios
adverbio_geral = r'RG'


# Pronomes
pronome_geral = r'P\w*'
pronome_pessoal_geral = r'PP\w*'


# Determinantes
determinante_geral = r'D\w*'
determinante_artigo_geral = r'DA\w*'


# Pontuação
pontuacao = r'F\w*'
pergunta = r'Fit'


# Expressões gerais
qualquer_palavra = r'\w*'
relax = r'relax'
verbos_lugar = (r'(ficar|estar|situar|localizar)')


Regexs['pergunta_lugar'] = {'exp': [
    (qualquer_palavra, adverbio_geral, None),
    (relax, pronome_pessoal_geral, None),
    (verbos_lugar, verbo_indicativo_presente_geral, 'verbo'),
    (relax, determinante_geral, None),
    (qualquer_palavra, nome_proprio_geral, 'lugar'),
    (relax, pergunta, None)
]}


Regexs['pergunta_pessoa'] = {'exp': [
    (qualquer_palavra, pronome_geral, None),
    (qualquer_palavra, verbo_geral, "verbo"),
    (qualquer_palavra, nome_proprio_geral, "nome"),
    (relax, pergunta, None)
]}


Regexs['nome_proprio'] = {'exp': [
    (relax, qualquer_palavra, None),
    (qualquer_palavra, nome_proprio_geral, 'nome_proprio'),
    (relax, qualquer_palavra, None),
    (relax, pontuacao, None)
]}


Regexs['nome_comum'] = {'exp': [
    (relax, qualquer_palavra, None),
    (qualquer_palavra, nome_comum_geral, 'nome_comum'),
    (relax, qualquer_palavra, None),
    (relax, pontuacao, None)
]}


def compile_regexs():
    global Regexs
    for regex in Regexs.keys():
        exp = Regexs[regex]['exp']
        s = r''
        for (word, type, group) in exp:
            if word == r'relax':
                if group:
                    aux = r'(' + type + r'\:' + '(?P<' + group + \
                        '>' + qualquer_palavra + r')){0,1}\s*'
                else:
                    aux = r'(' + type + r'\:' + qualquer_palavra + r'){0,1}\s*'
            else:
                if group:
                    aux = r'(' + type + r'\:' + \
                        '(?P<' + group + '>' + word + r'))\s*'
                else:
                    aux = r'(' + type + r'\:' + word + r')\s*'
            s = s + aux
        Regexs[regex] = re.compile(s)
    return Regexs


def parse_analise(analise):
    s = r''
    for (word, tag) in analise:
        aux = tag + r':' + word + r' '
        s = s + aux
    return s[:(len(s)) - 1]


def verifica(frase):
    matched = {}
    for reg_exp in Regexs.keys():
        res = Regexs[reg_exp].search(frase)
        if res:
            matched[reg_exp] = res.groupdict()
    return matched


Regexs = compile_regexs()
