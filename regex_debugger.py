#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from freeling_client import Client
from reg_exps import *

sock = Client()

print("Ligado ao servidor.")

def test_regex(frase):
    global sock
    sock.send(frase)
    return parse_analise(sock.recv())