#!/usr/bin/python3
# -*- coding: utf-8 -*-

class State:
    def __init__(self):
        self.dialogo = []

    def __str__(self):
        return 'Estado: '+len(self.dialogo) + " frases."

    def add(self, frase):
        self.dialogo.append(frase)

