#!/usr/bin/python3
# -*- coding: utf-8 -*-

import Wrappers.wikipedia_wrapper as wiki
import Wrappers.google_maps_wrapper as gmaps
import nltk


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

#TODO implementar a feature extraction do que foi analisado
#TODO implementar aqui o classificador
#TODO Criar um conjunto de treino
#TODO Criar um conjunto de teste

def features(pos, dep_tree, frase, exps_match):
    #TODO O que tirar de uma análise que seja relevante para a escolha de uma ação
    #TODO talvez começar por identificar o tipo de frase: Interrogação, Exclamação, etc
    #TODO aceder à BD de conhecimento local para determinar se as keywords extraídas dão alguma dica
    features = {}
    #Dummy approach
    exps = list(exps_match.keys())
    features['exp'] = exps[0]
    return features


train = []

classifier = nltk.classify.NaiveBayesClassifier.train(train)