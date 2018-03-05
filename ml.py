#!/usr/bin/python3
# -*- coding: utf-8 -*-


import csv, random, nltk


def mede_imp(exp):
    # Mede a importância de cada expressão
    return 1


def feature(exps):
    r'''
    Função que extraí a(s) features de uma frase analisada e comparada com as RegExs.
    :return:
    '''
    features = {}

    if len(exps) == 1:
        features['exp'] = exps[0]
        features['outras'] = []
    else:
        #Quando houve match com mais do que uma expressão
        #Definir uma função de medida de relevância para ver qual a expressão de maior importância e inserir ordenadamente.
        ordem = []
        for exp in exps:
            ordem += [(exp, mede_imp(exp))]
        ordem.sort(key=lambda exp:exp[1])
        features['exp'] = ordem[0]
        features['outras'] = ordem[1:]
    return features

def classificador():
    training_set = []
    devtest_set = []
    test_set = []
    # Criação do classificador
    classifier_NB = nltk.NaiveBayesClassifier.train(training_set)
    # Criação de uma lista de erros
    erros_NB = []
    for (name, tag) in devtest_set:
        a = feature(name)
        prob = classifier_NB.classify(a)
        if prob != tag:
            erros_NB.append((tag, prob, name))

    erros_NB_print = ''
    for (tag, prob, name) in erros_NB:
        erros_NB_print = erros_NB_print + 'Correto: ' + tag + '; Incorreto: ' + prob + '; Nome:' + name + '\n'
    precisao_NB = nltk.classify.accuracy(classifier_NB, test_set)

    #features_importantes = classifier.show_most_informative_features(7)
    #print(precisao)
    return classifier_NB, erros_NB, erros_NB_print, precisao_NB
