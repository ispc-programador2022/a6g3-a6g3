#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Recibe 2 valores enteros.
Retorna el modulo de 2 elementos(primero%segundo).
'''

def modulo(a,b):
    if type(a) == int and type(b) == int:
        return a%b
    else:
        return('Los valores ingresados son incorrectos.')

        