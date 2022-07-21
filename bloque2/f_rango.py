#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Función que calcule el rango del vector obtenido en genrnd.
'''
def rango_vector(vector):
    vector_unicos = []
    vector_repeticiones = []
    if len(vector) == 0:
        return None
    for elemento in vector:
        if elemento in vector_unicos:
            i = vector_unicos.index(elemento)
            vector_repeticiones[i] += 1
        else:
            vector_unicos.append(elemento)
            vector_repeticiones.append(1)
    rango = vector_unicos[0]
    maximo = vector_repeticiones[0]
    for i, elemento in enumerate(vector_unicos):
        if vector_repeticiones[i] > maximo:
            rango = vector_unicos[i]
            maximo = vector_repeticiones[i]
    return rango, maximo

    