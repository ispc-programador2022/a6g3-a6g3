#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Función que calcule la mediana del vector obtenido en genrnd. 
'''
def mediana(vector):
    a=int(len(vector)/2)
    vector.sort()
    return vector[a]

# Prueba
# from f_genrnd import genrnd
# lista=genrnd()
# print(mediana(lista))
# print(lista)