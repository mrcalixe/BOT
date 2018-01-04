#!/usr/bin/python3
# -*- coding: utf-8 -*-

from nltk.corpus import names
import csv, random, nltk, enchant

vogais = 'aeiou'
consoantes = 'qwrtypsdfghjklzxcvbnm'
# Ditongos decrescentes
ditongos_dec = ['ai', 'êi', 'ãi', 'ei', 'éi', 'oi', 'ói', 'ui', 'au', 'áu', 'eu', 'éu', 'iu', 'ou', 'ãe', 'ão', 'õe']
comb = ['qu', 'gu'] # Combinações
hiatos = ['ea', 'eo', 'ia', 'ie', 'io', 'oa', 'oe', 'ua', 'ue', 'ui', 'uo'] # Hiatos
consonanticos = (['b', 'c', 'd', 'f', 'g', 'p', 't', 'v'], ['l', 'r'])
digrafos = ['lh', 'nh', 'ch']


def divisao_silabas(palavra):
    s = [] # Sílabas
    i = 0
    j = 0
    while i < len(palavra):
        print("Estado - i:", i, "; j:", j, "; silabas [",s,"]")
        a = input("Continuar?")
        # Quando a 1ª palavra é consoante
        if palavra[i] in consoantes:
            # Caso apareça uma vogal, incrementa-se o i
            # para que o algorítmo passe pelos casos das vogais
            if palavra[i+1] in vogais:
                if palavra[i+1] == 'u' and palavra[i] in ['q','g']:
                    # Caso apareça um ditongo - divide-se com o ditongo
                    if (palavra[i+2]+palavra[i+3]) in ditongos_dec:
                        s.append(palavra[j : i+4])
                        i += 4
                        j = i
                    # Caso apareça uma vogal só, divide-se com a vogal
                    elif palavra[i+2] in vogais:
                        s.append(palavra[j : i+3])
                        i += 3
                        j = i
                elif i+2 == len(palavra) and palavra[i+2] in consoantes:
                    s.append(palavra[j : i+2])
                    i += 2
                    j = i
                    # Hiatos na silaba final
                elif (palavra[i] + palavra[i + 1]) in hiatos and i + 2 == len(palavra):
                    s.append(palavra[j: i + 3])
                    i += 3
                    j = i
                else:
                    i += 1
            # Caso de consoantes seguidas
            elif palavra[i+1] in consoantes:
                # Digrafos - Indivisível
                if (palavra[i]+palavra[i+1]) in digrafos:
                    i += 2
                # Grupo consonântico
                elif palavra[i] in consonanticos[0] and palavra[i+1] in consonanticos[1]:
                    # No prefixo, divisível
                    if len(s) == 0:
                        s.append(palavra[j : i+1])
                        i += 1
                        j = i
                    # Caso contrário, indivisível
                    else:
                        i += 2
                # Caso apareça cz ou ps no início da silaba - Indivisível
                elif len(s) == 0 and i==0 and (palavra[i]+palavra[i+1]) in ['cz', 'ps']:
                    i += 2
                # Caso contrário, onde se divide
                else:
                    s.append(palavra[j : i+1])
                    i += 1
                    j = i
        # Quando a 1ª palavra é vogal
        else:
            # Sequência de vogais
            if i+1 == len(palavra):
                s.append(palavra[j : i+1])
                i += 1
                j = i
            elif palavra[i+1] in vogais:
                # ditongos decrescentes - Indivisível
                if (palavra[i]+palavra[i+1]) in ditongos_dec:
                    i += 2
                # Hiatos na silaba final
                elif (palavra[i]+palavra[i+1]) in hiatos and i+2 == len(palavra):
                    s.append(palavra[j : i+2])
                    i += 2
                    j = i
                else:
                    s.append(palavra[j : i+1])
                    i += 1
                    j = i
            # Aparece uma consoante
            else:
                # Caso venha uma outra consoante que nao sejam consonanticas
                # Grupo consonântico
                if palavra[i+1] in consonanticos[0] and palavra[i+2] in consonanticos[1]:
                    # No prefixo, divisível
                    if len(s) == 0:
                        s.append(palavra[j: i + 2])
                        i += 2
                        j = i
                    # Caso contrário, indivisível
                    else:
                        i += 3
                # Caso contrário, onde se divide
                else:
                    s.append(palavra[j: i + 1])
                    i += 1
                    j = i
    #Ao testar com admirador dá erro
    return s



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