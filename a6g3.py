#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Funcion que invoca al resto de la funciones.
'''

from msilib import type_key
from tkinter import E
import bloque1.f_cociente as cociente
import bloque1.f_ing2i as ing2i
import bloque1.f_ing2s as ing2s
import bloque1.f_modulo as modulo
import bloque1.f_p1 as p1
import bloque1.f_potencia as potencia
import bloque1.f_presentacion as presentacion
import bloque1.f_producto as producto
import bloque1.f_radicacion as radicacion
import bloque1.f_resta as resta
import bloque1.f_suma as suma


def tipo_dato(dato):
    if isinstance(dato, int):
        res = 'int'
    elif isinstance(dato, str):
        res = 'str'
    elif isinstance(dato, list):
        res = 'list'
    elif isinstance(dato, tuple):
        res = 'tuple'
    return res



presentacion.funcionPresentacion()
print()
print()

print('Funcion ing2i, pide el ingreso de dos valores del tipo entero')
enteros = ing2i.ing2i()
print()
print('Funcion ing2s, pide el ingreso de dos valores del tipo string')
strings = ing2s.ing2s()
print()
print('Los valores ingresados son: ')

print(f'''
Valores ingresados: {enteros[0]} -> {tipo_dato(enteros[0])}       {enteros[1]} -> {tipo_dato(enteros[1])}
                    {strings[0]} -> {tipo_dato(strings[0])}       {strings[1]} -> {tipo_dato(strings[1])}
''')
print()

print('='*50)
print()

print('\nRetorno de la funcion f_suma: ', suma.suma(enteros[0], enteros[1]), end='\n')
print('\nRetorno de la funcion f_resta: ', resta.resta(enteros[0], enteros[1]), end='\n')
print('\nRetorno de la funcion f_producto: ', producto.producto(enteros[0], enteros[1]), end='\n')
print('\nRetorno de la funcion f_cociente: ', cociente.cociente(enteros[0], enteros[1]), end='\n')
print('\nRetorno de la funcion f_modulo: ', modulo.modulo(enteros[0], enteros[1]), end='\n')
print('\nRetorno de la funcion f_potencia: ', potencia.potencia(enteros[0], enteros[1]), end='\n')
print('\nRetorno de la funcion f_radicacion: ', radicacion.radicacion(enteros[0], enteros[1]), end='\n')

# entero3 = int(input('ingrese el 3 entero: '))
fp1 = p1.p1(enteros[0], enteros[1])
a=enteros[0]
b=enteros[1] 
c=fp1[3]
print('\nRetorno de la funcion f_p1: ',f'''
                            {a} * {b} + {c} = {fp1[0]}
                            ({a} + {b}) * {c} ={fp1[1]}
                            ({a} - {b}) * {c} ={fp1[2]}''')


