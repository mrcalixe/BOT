#!/usr/bin/python3
# -*- coding: utf-8 -*-

import FreeLing_Client.freeling_client as freeling
import Exps_Regulares.new_reg_exps as reg
import nltk

frase = "Onde fica o Porto?"

def do(f):
    analyzed = freeling.analyse(f)
    dot, tagged = freeling.extract(analyzed['sentences'][0])
    parsed_tag = reg.parse_analise(tagged)
    print("=============Análise=============")
    print(parsed_tag)
    print("=================================")
    v1 = reg.verifica(parsed_tag)
    v2 = reg.verifica_especiais(parsed_tag)
    v3 = reg.verifica_backup(parsed_tag)
    return v1,v2,v3