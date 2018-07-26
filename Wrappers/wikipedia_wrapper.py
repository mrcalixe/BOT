#!/usr/bin/python3
# -*- coding: utf-8 -*-

import wikipedia as wiki

# DBPEDIA


wiki.set_lang('pt')


# TODO Ir buscar mais informação referente à pesquisa. Exemplo: tipos, tags, keywords, ...


def procura_nome(nome, frases=1):
    return wiki.summary(nome, sentences=frases)
