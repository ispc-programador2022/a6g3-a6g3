#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Recibe 2 valores enteros.
Retorna la raiz del primero respecto del segundo parámetros.
'''
def radicacion(a,b):
    if type(a) == int and type(b) == int:
        return b**(1/a)
    else:
        print('Los valores ingresados no son correctos.\nInténtelo nuevamente.')
        pass

#Probar
#radicacion(2,3)