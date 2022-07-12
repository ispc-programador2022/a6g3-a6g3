#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Recibe 2 valores enteros.
Retorna la potencia del primero elevado al segundo parámetros.
'''
def potencia(a,b):       
    if type(a) == int and type(b) == int:
        return a**b
    else:
        print('Los valores ingresados no son correctos.\nInténtelo nuevamente.')
        pass

#Probar
#potencia(2,3)