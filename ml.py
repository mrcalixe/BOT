#!/usr/bin/python3
# -*- coding: utf-8 -*-

import nltk



def features(analise):
    r'''
    Função que extraí a(s) features de uma frase analisada e comparada com as RegExs.
    Recebe o dicionário das análises efetuadas, com as expressões regulares e os respetivos grupos "apanhados"
    '''
    features = {}
    features['exps'] = analise.keys()
    return analise


def classificador(train):
    for t in train.keys():
        print(t)
    training_set = []
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
