#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re

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


# Interjeição
interjeicao = r'I'
interjeicao_intro = r'(olá|boas)'
interjeicao_outro = r'(xau|adeus)'

# Expressões gerais
qualquer_palavra = r'\w*'
relax = r'relax'
verbos_lugar = r'(ficar|estar|situar|localizar)'


##########################################################################################

Regexs = {}

Regexs['pergunta_lugar'] = {'exp': [
    (qualquer_palavra, adverbio_geral, None),
    (relax,            pronome_pessoal_geral, None),
    (verbos_lugar,     verbo_indicativo_presente_geral, None),
    (relax,            determinante_geral, None),
    (qualquer_palavra, nome_proprio_geral, 'locality'),
    (relax,            pergunta, None)
], 'action': 'procura_lugar'}


Regexs['pergunta_pessoa'] = {'exp': [
    (qualquer_palavra, pronome_geral, None),
    (qualquer_palavra, verbo_geral, None),
    (qualquer_palavra, nome_proprio_geral, "name"),
    (relax, pergunta, None)
], 'action': 'pergunta_pessoa'}


##########################################################################################

Regexs_Backup = {}

Regexs_Backup['nome'] = {'exp': [
    (relax, qualquer_palavra, None),
    (qualquer_palavra, nome_geral, 'name'),
    (relax, qualquer_palavra, None)
], 'action': 'pergunta_nome'}

##########################################################################################

Regexs_Especiais = {}

Regexs_Especiais['intro'] = {'exp': [
    (relax, qualquer_palavra, None),
    (interjeicao_intro, interjeicao, 'interjeicao'),
    (relax, qualquer_palavra, None)
], 'action': 'bem_vindo'}

Regexs_Especiais['outro'] = {'exp': [
    (relax, qualquer_palavra, None),
    (interjeicao_outro, interjeicao, 'interjeicao'),
    (relax, qualquer_palavra, None)
], 'action': 'adeus'}

##########################################################################################


def compile_regexs(Regexs):
    for regex in Regexs.keys():
        exp = Regexs[regex]['exp']
        s = r''
        for (word, tipo, group) in exp:
            if word == r'relax':
                if group:
                    aux = r'(' + tipo + r'\:' + '(?P<' + group + \
                        '>' + qualquer_palavra + r')){0,1}\s*'
                else:
                    aux = r'(' + tipo + r'\:' + qualquer_palavra + r'){0,1}\s*'
            else:
                if group:
                    aux = r'(' + tipo + r'\:' + \
                        '(?P<' + group + '>' + word + r'))\s*'
                else:
                    aux = r'(' + tipo + r'\:' + word + r')\s*'
            s = s + aux
        Regexs[regex]['exp'] = re.compile(s, re.IGNORECASE)
    return Regexs


def parse_analise(analise):
    s = r''
    for (word, tag) in analise:
        aux = tag + r':' + word + r' '
        s = s + aux
    return s[:(len(s)) - 1]


def verifica_especiais(frase):
    matched = {}
    for reg_exp in Regexs_Especiais.keys():
        res = Regexs_Especiais[reg_exp]['exp'].search(frase)
        if res:
            matched[reg_exp] = res.groupdict()
    return matched

def verifica(frase):
    matched = {}
    for reg_exp in Regexs.keys():
        res = Regexs[reg_exp]['exp'].search(frase)
        if res:
            matched[reg_exp] = res.groupdict()
    return matched


def verifica_backup(frase):
    matched = {}
    for reg_exp in Regexs_Backup.keys():
        res = Regexs_Backup[reg_exp]['exp'].search(frase)
        if res:
            matched[reg_exp] = res.groupdict()
    return matched


Regexs = compile_regexs(Regexs)
Regexs_Backup = compile_regexs(Regexs_Backup)
Regexs_Especiais = compile_regexs(Regexs_Especiais)
