#!/usr/bin/python3
# -*- coding: utf-8 -*-

import FreeLing_Client.freeling_client
from Exps_Regulares.reg_exps import *

sock = FreeLing_Client.freeling_client.Client()

def test_regex(frase):
    global sock
    sock.send(frase)
    return parse_analise(sock.recv())