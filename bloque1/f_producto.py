#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Recibe 2 valores enteros.
Retorna el producto de los 2 elementos.
'''

def producto(a,b):
    if type(a) == int and type(b) == int:
        return a*b
    else:
        return('Los valores ingresados son incorrectos.')

