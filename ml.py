#!/usr/bin/python3
# -*- coding: utf-8 -*-

from nltk.corpus import names
import csv, random, nltk, enchant

dic = enchant.Dict("pt_PT")

vogais = 'aeiou'
consoantes = 'qwrtypsdfghjklzxcvbnm'
# Ditongos decrescentes
acentuadas = ['á', 'à', 'ã', 'â', ]
ditongos_dec = ['ai', 'êi', 'ãi', 'ei', 'éi', 'oi', 'ói', 'ui', 'au', 'áu', 'eu', 'éu', 'iu', 'ou', 'ãe', 'ão', 'õe']
comb = ['qu', 'gu'] # Combinações
hiatos = ['ea', 'eo', 'ia', 'ie', 'io', 'oa', 'oe', 'ua', 'ue', 'ui', 'uo'] # Hiatos
consonanticos = (['b', 'c', 'd', 'f', 'g', 'p', 't', 'v'], ['l', 'r'])
digrafos = ['lh', 'nh', 'ch']


#Regras da divisão
#Ditongo decrescente
def check_ditongo_dec(palavra, i):
    if i+1 == len(palavra):
        return False
    elif (palavra[i] + palavra[i+1]) in ditongos_dec:
        return True
    else:
        return False


def check_hiato(palavra, i):
    if (palavra[i] + palavra[i+1]) in hiatos:
        return True
    else:
        return False


def check_vog_dulpa(palavra, i):
    if palavra[i] in vogais and palavra[i+1] == palavra[i]:
        return True
    else:
        return False


def check_comb(palavra, i):
    if (palavra[i] + palavra[i+1]) in comb:
        return True
    else:
        return False


def check_consonantico(palavra, i):
    if i == 0 and (palavra[i] + palavra[i + 1]) in ['cz', 'ps']:
        return True
    elif palavra[i] in consonanticos[0] and palavra[i+1] in consonanticos[1]:
        return True
    else:
        return False


def check_digrafo(palavra, i):
    if (palavra[i] + palavra[i+1]) in digrafos:
        return True
    else:
        return False


def div_silabas_aux(p):
    p = p.lower()
    s = []
    i, j = 0, 0
    dividir = False
    while i<len(p):
        #print('------------------------------------------\ni:', i, 'j:', j, 'sílabas:', s, 'dividir?', dividir)
        #a = input('Continuar?')
        if p[i] in vogais:
            #print('Vogal:', p[i])
            if i == len(p)-1:
                i += 1
                s.append(p[j: i])
                j = i
            #Inidivisivel
            elif check_ditongo_dec(p, i):
                #print('Ditongo decrescente')
                i += 1
            elif check_hiato(p, i) and  i+2 == len(p):#Quando é um hiato na sílaba final
                if i-j >= 2:
                    i += 1
                    s.append(p[j : i])
                    j = i
                else:
                    #print('Hiato na última sílaba')
                    i += 2
                    if i==len(p):
                        s.append(p[j : i])
            #Divisivel
            elif check_hiato(p, i) or check_vog_dulpa(p, i):
                #print('Hiato ou vogal dupla')
                i += 1
                s.append(p[j : i])
                j = i
            else:
                if i == len(p)-1:
                    i += 1
                    s.append(p[j: i])
                    j = i
                else:
                    dividir = True
                    i += 1
        else:#Quando encontramos uma consoante
            #print('Consoante:', p[i])
            if i == len(p)-1:
                i += 1
                s.append(p[j: i])
                j = i
            elif check_consonantico(p, i):
                #print('Grupo consonantico')
                #Divisivel
                if len(s) == 0 and p[i+1] in ['b', 'd']:
                    #print('Grupo consonantico que acaba em b ou d é está num prefixo')
                    i += 2
                    s.append(p[j : i])
                    j = i
                #Indivisivel
                else:
                    if dividir:
                        s.append(p[j : i])
                        j = i
                        i += 2
                        dividir = False
                    else:
                        i += 2
            #Indivisivel
            elif check_digrafo(p, i):
                #print('Dígrafo')
                if dividir:
                    s.append(p[j: i])
                    j = i
                    i += 2
                    dividir = False
                else:
                    i += 2
            #Indivisivel
            elif check_comb(p, i):
                #print('Combinação')
                #Verificar se um ditongo
                if check_ditongo_dec(p, i+2):
                    i += 4
                    s.append(p[j : i])
                    j = i
                #Verificar se é uma vogal
                elif p[i+2] in vogais:
                    i += 3
                    s.append(p[j : i])
                    j = i
                else:
                    i += 1
            else:
                #Se for uma sequencia de consoantes, divide-se
                if p[i+1] in consoantes:
                    i += 1
                    s.append(p[j : i])
                    j = i
                    if dividir:
                        dividir = False
                elif dividir:
                    s.append(p[j: i])
                    j = i
                    i += 1
                    dividir = False
                else:
                    i += 1

    return s


def div_silabas(p):
    #print('Em:', p)
    if '-' in p:
        p2 = p.split('-')
        silabas = []
        for i in range(len(p2)):
            silabas = silabas + div_silabas_aux(p2[i])
            if i < len(p2)-1:
                silabas = silabas + ['-']
    else:
        silabas = div_silabas_aux(p)

    return silabas




def silaba_tonica(s):
    #Verificar acentos:
    try:
        teste = s.encode('ascii')
    except UnicodeEncodeError as uee:
        #Tem acentos
        #Verificar se a última sílaba termina com vogais(s)
        i = s[len(s) - 1]
        if len(i) >= 2:
            if i[-2:len(i)] in ['os', 'as', 'es']:
                return len(s)-1
        else:
            if i[-1] in ['o', 'a', 'e']:
                return len(s)-1


def gender_feature(word):
    s = div_silabas(word)
    features = {}
    #features['ultima_silaba'] = s[-1]
    #features['p_silabas'] = s[0]
    features['u_silabas'] = s[-1]
    #features['vogais'] = len([x for x in word if x in vogais])
    #features['consoantes'] = len([x for x in word if x in consoantes])
    return features


def load_nomes():
    nomes = []
    with open('nomes_clean.csv') as csvin:
        nomes = [(row[0], row[1]) for row in csv.reader(csvin)]
        random.shuffle(nomes)
        return nomes

nomes = load_nomes()


def classificador_genero(nomes, train_size=500, erros_size=300):
    set_size = len(nomes)
    #print(set_size, 'Nomes')
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
    erros_pretty_print = ''
    for (tag, prob, name) in erros:
        erros_pretty_print = erros_pretty_print + 'Correto: ' + tag + '; Incorreto: ' + prob + '; Nome:' + name + '\n'
    precisao = nltk.classify.accuracy(classifier, test_set)
    #features_importantes = classifier.show_most_informative_features(7)
    #print(precisao)
    return classifier, erros, erros_pretty_print, precisao



