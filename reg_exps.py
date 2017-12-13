# -*- coding: utf-8 -*-
import re

# Responder a perguntas:
#   Quem canta ...?
regex_asking_who_sings = re.compile("Quem canta [a-zA-Z]+?")
#   Foi ... quem cantou ...?
regex_asking_who_sings2 = re.compile("Foi [a-zA-Z]+ quem cantou [a-zA-Z]+?")
#   Quem é ...?
regex_artist_search = re.compile("Quem é [a-zA-Z]+?")