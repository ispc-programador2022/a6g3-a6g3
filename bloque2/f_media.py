#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Función que calcule la media del vector obtenido en genrnd.

Calculo la media aritmética (por defecto, ya que no se especifica
que media se debe calcular)
'''


def media(vector):
    res = 0
    for i in vector:
        res = res + i
    med = res/len(vector)
    return med

#Test
# import random
# import f_genrnd
# lista = f_genrnd.genrnd()
# print(media(lista))