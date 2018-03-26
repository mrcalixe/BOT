#!/usr/bin/python3
# -*- coding: utf-8 -*-

import nltk

from reg_exps import *


def features(frase):
    r'''
    Função que extraí a(s) features de uma frase analisada e comparada com as RegExs.
    Recebe uma lista de pares, com a expressão e o respetivo dicionário das análises efetuadas, com as expressões regulares e os respetivos grupos "apanhados"
    '''
    analise = verifica(frase)
    features = {}
    features['keywords'] = []
    features['exps'] = []
    for (exp, dic) in analise:    
        for k in dic.keys():
            features['keywords'] += [dic[k]]
        features['exps'] += analise.keys()
    return features


'''O classificador pega numa analise do FreeLing, e escolhe uma ação. Ou seja, a função feature vai ter de correr a função verifica das reg_exps,
e depois extrair o conhecimento que for necessário.'''


def classificador(treino_dict):
    '''"Onde fica Braga?" : {"action" : "procura_lugar", "keywords" : ["lugar", "verbo"]},
    "Quem é Mozart?"   : {"action" : "procura_pessoa", "keywords" : ["nome", "verbo"]},
    "Onde se situa o Porto?" : {"action" : "procura_lugar", "keywords" : ["lugar", "verbo"]}'''
    training_set = [ (k, treino_dict[k]['action']) for k in treino_dict.keys()]
    devtest_set = []
    # Criação do classificador
    classifier_NB = nltk.NaiveBayesClassifier.train(training_set)
    # Criação de uma lista de erros
    erros_NB = []
    for (name, tag) in devtest_set:
        a = features(name)
        prob = classifier_NB.classify(a)
        if prob != tag:
            erros_NB.append((tag, prob, name))

    erros_NB_print = ''
    for (tag, prob, name) in erros_NB:
        erros_NB_print = erros_NB_print + 'Correto: ' + tag + \
            '; Incorreto: ' + prob + '; Nome:' + name + '\n'
    #precisao_NB = nltk.classify.accuracy(classifier_NB, test_set)

    #features_importantes = classifier.show_most_informative_features(7)
    # print(precisao)
    return classifier_NB, erros_NB, erros_NB_print #, precisao_NB
