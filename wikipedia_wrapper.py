#!/usr/bin/python3
# -*- coding: utf-8 -*-

import wikipedia as wiki


wiki.set_lang('pt')


def procura_nome(nome, frases = 1):
    return wiki.summary(nome, sentences=frases)