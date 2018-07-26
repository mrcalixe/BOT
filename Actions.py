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



def get_action_from_frase(frase, db):
    sql_command = """SELECT action FROM Frases WHERE frase = '{frase}';"""
    db.cursor.execute(sql_command.format(frase=frase))
    data = db.cursor.fetchone()
    res = []
    while data:
        res.append(data[0])
        data = db.cursor.fetchone()
    return res



def get_keywords(key, db):
    sql_command = """SELECT keyword FROM Keywords WHERE keyword LIKE '{key}';"""
    db.cursor.execute(sql_command.format(key=key))
    data = db.cursor.fetchone()
    res = []
    while data:
        res.append(data[0])
        data = db.cursor.fetchone()
    return res



def features(frase, analise, exps, db_keys, db_frases, dep_tree=None):
    #TODO O que tirar de uma análise que seja relevante para a escolha de uma ação
    #TODO talvez começar por identificar o tipo de frase: Interrogação, Exclamação, etc
    #TODO aceder à BD de conhecimento local para determinar se as keywords extraídas dão alguma dica

    ###################################
    #          Frases                 #
    ###################################
    frases = {}
    # Vai buscar as ações através da correspondências do modelo linguistico
    actions_from_exp = [a for exp in exps for a in mapa_acoes[exp]]
    # Vai buscar as ações associadas a frases conhecidas.
    actions_from_knowledge = get_action_from_frase(frase, db_frases)
    ###################################
    #          Keywords               #
    ###################################
    keys = {}
    #Keys vindas das análises que estão no conhecimento
    keys1 = [get_keywords(exps[exp][exp2], db_keys) for exp in exps for exp2 in exps[exp]]
    ###################################
    #          Features               #
    ###################################
    features = {}
    features['action'] = actions_from_exp[0]
    features['keyword'] = keys1[0][0]

    return actions_from_exp, actions_from_knowledge, keys1, features


from sklearn.naive_bayes import BernoulliNB



train_set = [('Onde fica Braga?',       'procura_lugar'),
             ('Onde se situa o Porto?', 'procura_lugar'),
             ('Quem é Mozart?',         'procura_pessoa')]

train_set_2 = [('Onde_fica_Braga?',       'procura_lugar'),
              ('Onde_se_situa_o_Porto?', 'procura_lugar'),
              ('Quem_é_Mozart?',         'procura_pessoa')]

# classifier = nltk.NaiveBayesClassifier(train_test)

# classifier.train(train_test)
