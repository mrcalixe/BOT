#!/usr/bin/python3
# -*- coding: utf-8 -*-

from nltk.corpus import names
import csv, random, nltk, enchant

vogais = 'aeiou'
consoantes = 'qwrtypsdfghjklzxcvbnm'


# NAO ACABADA
def divisao_silabas2(palavra):
    if len(palavra) == 0:
        return []
    elif 1 <= len(palavra) <= 2:
        return [palavra]
    elif True:
        return []


# ERRADA - A tentar construir de forma recursiva pois é mais acertada e simples
def divisao_silabas(palavra):
    silabas = []
    limite = len(palavra)-1
    aux = ''
    i = 0
    while i < len(palavra):
        aux = aux+palavra[i]
        if palavra[i+1] in consoantes and palavra[i+2] in consoantes:
            aux = aux+palavra[i+1]
            i += 2
            silabas.append(aux)
            aux = ''
        elif palavra[i+1] in consoantes and palavra[i+2] in vogais:
            #aux = aux + pala vra[i]
            i += 1
            silabas.append(aux)
            aux = ''
        elif palavra[i+1] in vogais and palavra[i+2] in consoantes:
            #aux = aux + palavra[i]
            silabas.append(aux)
            aux = ''+palavra[i+1]
            i += 2
            silabas.append(aux)
            aux = ''
        else:
            aux = ''
            break
    return silabas


def gender_feature(word):
    word = word.lower()
    features = {}
    i = len(word)
    #features['primeiras_letras'] = word[0: 2]
    features['ultimas_letras'] = word[-2:]
    #features['vogais'] = len([x for x in word if x in vogais])
    #features['consoantes'] = len([x for x in word if x in consoantes])
    return features

nomes = []
with open('nomes_clean.csv') as csvin:
    nomes = [(row[0], row[1]) for row in csv.reader(csvin)]
    random.shuffle(nomes)

set_size = len(nomes)
#print(set_size, 'Nomes')

train_size = 500
erros_size = 300
# Conjuntos de nomes
training_names = nomes[:train_size]
devtest_names = nomes[train_size:train_size+erros_size]
test_names = nomes[:set_size-(train_size+erros_size)]


# Conjuntos que para o classificador
training_set = [(gender_feature(n), g) for (n, g) in training_names if gender_feature(n)]
devtest_set = [(gender_feature(n), g) for (n, g) in devtest_names if gender_feature(n)]
test_set = [(gender_feature(n), g) for (n, g) in test_names if gender_feature(n)]


# Criação do classificador
classifier = nltk.NaiveBayesClassifier.train(training_set)


# Criação de uma lista de erros
erros = []
for (name, tag) in devtest_names:
    a = gender_feature(name)
    prob = classifier.classify(a)
    if prob != tag:
        erros.append((tag, prob, name))

# Print dos erros do classificador, para encontrar novos padrões, ou casos extremos
#print('Erros do classificador')
#for (tag, prob, name) in erros:
#    print('Correto:',tag,'; Incorreto:',prob,'; Nome:',name)

precisao = nltk.classify.accuracy(classifier, test_set)
#features_importantes = classifier.show_most_informative_features(7)

#print(precisao)