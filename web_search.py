#!/usr/bin/python3
# -*- coding: utf-8 -*-

import wikipedia as wiki

wiki.set_lang('pt')


def get_n_frases(frase, n):
    i = 0
    res = ""
    for j in frase:
        res = res + j
        if j == '.':
            i += 1
            if i == n:
                break
    return res


def procura_lugar(nome):
    return wiki.summary(nome, sentences=1)