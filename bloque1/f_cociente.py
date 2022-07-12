#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Recibe 2 valores enteros.
Retorna el cociente de los 2 elementos.
'''


def cociente(numerador,denominador):
    if type(numerador) == int and type(denominador) == int:
        if denominador != 0:
            return numerador/denominador
        else:
            return("El denominador no puede ser cero.")
    else:
        return("Los números ingresados no son enteros.")