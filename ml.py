#!/usr/bin/python3
# -*- coding: utf-8 -*-

from nltk.corpus import names
import csv, random, nltk

def gender_feature(word):
    features = {}
    i = len(word)
    features['last_letters'] = word[i - 3: i]
    features['first_letters'] = word[0:3]
    return features


with open('nomes_clean.csv') as csvin:
    nomes = [(row[0], row[1])  for row in csv.reader(csvin)]
    random.shuffle(nomes)

feature_set = [(gender_feature(n), gender) for (n,gender) in nomes]
train_size = 200
train_set, test_set = feature_set[train_size:], feature_set[:14176-train_size]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print(nltk.classify.accuracy(classifier, test_set))

print(classifier.classify(gender_feature('Carlos')))
print(classifier.classify(gender_feature('Elza')))
print(classifier.classify(gender_feature('Beatriz')))
print(classifier.classify(gender_feature('Leonor')))
print(classifier.show_most_informative_features(5))