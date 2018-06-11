#!/usr/bin/python3
# -*- coding: utf-8 -*-

import Wrappers.wikipedia_wrapper as wiki
import Wrappers.google_maps_wrapper as gmaps


def pergunta_nome(**kargs):
    print(__name__, ':kargs:', kargs)
    if kargs['dict']:
        return wiki.procura_nome(kargs['dict']['name'])
    else:
        return 'Não consegui entender o nome...'

def pergunta_pessoa(**kargs):
    print(__name__, ':kargs:', kargs)
    if kargs['dict']:
        return wiki.procura_nome(kargs['dict']['name'])
    else:
        return 'Não consegui entender o nome da pessoa...'

def procura_lugar(**kargs):
    print(__name__, ':kargs:', kargs)
    if kargs['dict']:
        return gmaps.procura_lugar(kargs['dict']['locality'])
    else:
        return 'Não consegui entender o lugar...'

def bem_vindo(**kargs):
    print(__name__, ':kargs:', kargs)
    if kargs['dict']:
        return 'Olá ' + (kargs['dict']['name']).capitalize() + ', prazer em conhecer :)'
    else:
        return 'Olá :)'

def adeus(**kargs):
    print(__name__, ':kargs:', kargs)
    return 'Até à próxima :)'