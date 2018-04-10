#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random

def oneOf(arr):
    # Simples função que escolhe aleatóriamente um elemento de um array
    rand_idx = random.randint(0,len(arr) - 1)
    return arr[rand_idx]
