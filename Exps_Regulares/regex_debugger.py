#!/usr/bin/python3
# -*- coding: utf-8 -*-

from freeling_client import Client
from Exps_Regulares.reg_exps import *

sock = Client()

print("Ligado ao servidor.")

def test_regex(frase):
    global sock
    sock.send(frase)
    return parse_analise(sock.recv())