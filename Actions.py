#!/usr/bin/python3
# -*- coding: utf-8 -*-

import Wrappers.wikipedia_wrapper as wiki
import Wrappers.google_maps_wrapper as gmaps
import nltk
from Exps_Regulares.new_reg_exps import mapa_acoes
from DB2 import DB_Frases, DB_Keywords, connection


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



def get_action_from_frase(frase, db=DB_Frases):
    sql_command = """SELECT action FROM Frases WHERE frase = '{frase}';"""
    db.cursor.execute(sql_command.format(frase=frase))
    data = db.cursor.fetchone()
    res = []
    while data:
        res.append(data[0])
        data = db.cursor.fetchone()
    return res



def get_keywords(key, db=DB_Keywords):
    sql_command = """SELECT keyword FROM Keywords WHERE keyword LIKE '{key}';"""
    db.cursor.execute(sql_command.format(key=key))
    data = db.cursor.fetchone()
    res = []
    while data:
        res.append(data[0])
        data = db.cursor.fetchone()
    return res



def features(frase, analise, dep_tree, exps, db_keys, db_frases):
    #TODO O que tirar de uma análise que seja relevante para a escolha de uma ação
    #TODO talvez começar por identificar o tipo de frase: Interrogação, Exclamação, etc
    #TODO aceder à BD de conhecimento local para determinar se as keywords extraídas dão alguma dica

    ###################################
    #          Frases                 #
    ###################################
    frases = {}
    # Vai buscar as ações através da correspondências do modelo linguistico
    actions_from_exp = [mapa_acoes[exp] for exp in exps]
    # Vai buscar as ações associadas a frases conhecidas.
    actions_from_knowledge = get_action_from_frase(frase)
    ###################################
    #          Keywords               #
    ###################################
    keys = {}
    #Keys vindas das análises que estão no conhecimento
    keys1 = [get_keywords(exps[exp][exp2]) for exp in exps for exp2 in exp]
    ###################################
    #          Features               #
    ###################################
    features = {}


    return actions_from_exp, actions_from_knowledge, keys1


from sklearn.naive_bayes import BernoulliNB



train_test = []

classifier = nltk.NaiveBayesClassifier(train_test)

classifier.train(train_test)