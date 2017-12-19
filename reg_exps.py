# -*- coding: utf-8 -*-
import re

# Responder a perguntas:
#   Quem canta ...?
regex_asking_who_sings = re.compile("Quem (cantou|canta) (?P<music>[a-zA-Z0-9 ]+)\?")
#   Foi ... quem cantou ...?
regex_asking_who_sings2 = re.compile("(Foi|Foram) (o|os|a|as)* (?P<artist>[a-zA-Z0-9 ]+)(quem|que) (cantaram|cantou) (?P<music>[a-zA-Z0-9 ]+)\?")
#   Quem é ...?
regex_artist_search = re.compile("Quem é (?P<artist>[a-zA-Z0-9 ]+)\?")
