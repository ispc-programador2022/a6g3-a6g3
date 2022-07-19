#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
función genrnd que retorna una lista con 50 números aleatorios.
'''

import random

def genrnd():
    lista_rnd = []
    for i in range(50):
        lista_rnd.append(random.randint(0,1000))
    return lista_rnd

#Test
#print(genrnd())
