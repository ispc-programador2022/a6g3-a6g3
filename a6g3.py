#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Funcion que invoca al resto de la funciones.
'''


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

import bloque2.f_cociente_comb as cociente_comb
import bloque2.f_genrnd as genrnd
import bloque2.f_maximo_vector as maximo_vector
import bloque2.f_media as media
import bloque2.f_mediana as mediana
import bloque2.f_minimo_vector as minimo_vector
import bloque2.f_producto_comb as producto_comb
import bloque2.f_rango as rango
import bloque2.f_suma_comb as suma_comb
import bloque2.f_varianza as varianza

import bloque3.f_genrnd_ as genrnd_
import bloque3.f_maximo_ as maximo_
import bloque3.f_media_ as media_
import bloque3.f_mediana_ as mediana_
import bloque3.f_minimo_ as minimo_
import bloque3.f_rango_ as rango_
import bloque3.f_tiempo_bloque2 as tiempo_b2
import bloque3.f_tiempo_bloque3 as tiempo_b3
import bloque3.f_varianza_ as varianza_


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


#===================        Bloque 1        ======================#
presentacion.funcionPresentacion()
print()
print()

print('Funcion ing2i, pide el ingreso de dos valores del tipo entero')
enteros = ing2i.ing2i()
print()
print('Funcion ing2s, pide el ingreso de dos valores del tipo string')
strings = ing2s.ing2s()
print()
#print('Los valores ingresados son: ')

print(f'''
Valores ingresados: {enteros[0]} -> {tipo_dato(enteros[0])}       {enteros[1]} -> {tipo_dato(enteros[1])}
                    {strings[0]} -> {tipo_dato(strings[0])}       {strings[1]} -> {tipo_dato(strings[1])}
''')
print()

print('='*100)
print('\nRetornos de las funciones del Bloque 1\n')

print('\nRetorno de la funcion f_suma: ', suma.suma(enteros[0], enteros[1]), end='\n')
print('\nRetorno de la funcion f_resta: ', resta.resta(enteros[0], enteros[1]), end='\n')
print('\nRetorno de la funcion f_producto: ', producto.producto(enteros[0], enteros[1]), end='\n')
print('\nRetorno de la funcion f_cociente: ', cociente.cociente(enteros[0], enteros[1]), end='\n')
print('\nRetorno de la funcion f_modulo: ', modulo.modulo(enteros[0], enteros[1]), end='\n')
print('\nRetorno de la funcion f_potencia: ', potencia.potencia(enteros[0], enteros[1]), end='\n')
print('\nRetorno de la funcion f_radicacion: ', radicacion.radicacion(enteros[0], enteros[1]), end='\n')

print('\n')
fp1 = p1.p1(enteros[0], enteros[1])
a=enteros[0]
b=enteros[1] 
c=fp1[3]
print('\nRetorno de la funcion f_p1: ',f'''
                            {a} * {b} + {c} = {fp1[0]}
                            ({a} + {b}) * {c} ={fp1[1]}
                            ({a} - {b}) * {c} ={fp1[2]}''')
print('\n')
#===================        Bloque 2        ======================#
print('='*100)
print('\nRetornos de las funciones del Bloque 2\n')
vector_corto = genrnd.genrnd()
#print('\nRetorno de la funcion f_suma_comb: ', suma_comb.suma_comb(vector_corto), end = '\n')
#print('\nRetorno de la funcion f_cociente_comb:  ', cociente_comb.cociente(vector_corto), end = '\n')
print('\nRetorno de la funcion f_producto_comb: ', producto_comb.producto_comb1(vector_corto), end = '\n')
print('\nRetorno de la funcion f_producto_comb: ', producto_comb.producto_comb2(vector_corto), end = '\n')
print('\nRetorno de la funcion f_producto_comb: ', producto_comb.producto_comb3(vector_corto), end = '\n')
print('\nRetorno de la funcion f_media: ', media.media(vector_corto), end = '\n')
print('\nRetorno de la funcion f_mediana: ', mediana.mediana(vector_corto), end = '\n')
print('\nRetorno de la funcion f_rango: ', rango.rango_vector(vector_corto), end = '\n')
print('\nRetorno de la funcion f_varianza: ', varianza.varianza(vector_corto), end = '\n')
print('\nRetorno de la funcion f_minimo_vector: ', minimo_vector.minimo_del_vector(vector_corto), end = '\n')
print('\nRetorno de la funcion f_maximo_vector: ', maximo_vector.maximo_del_vector(vector_corto), end = '\n')

print()

#===================        Bloque 3        ======================#
print('='*100)
print('\nRetornos de las funciones del Bloque 2\n')

vector_largo = genrnd_.genrnd()

#print('\nRetorno de la funcion f_media_: ', media_.media_(vector_largo), end = '\n')
#print('\nRetorno de la funcion f_mediana_: ', mediana_.mediana_(vector_largo), end = '\n')
#print('\nRetorno de la funcion f_rango_: ', rango_.rango_(vector_largo), end = '\n')
#print('\nRetorno de la funcion f_varianza_: ', varianza_.varianza_(vector_largo), end = '\n')
print('\nRetorno de la funcion f_minimo_vector_: ', minimo_.minimo_del_vector(vector_largo), end = '\n')
print('\nRetorno de la funcion f_maximo_vector_: ', maximo_.maximo_del_vector(vector_largo), end = '\n')

print('\nComparación en los tiempos de ejecucion de los bloques 2 y 3 (mismas funciones): ', end='\n')
#print('\nTiempo de ejecucion del bloque 2: ', tiempo_b2.tiempo(), end='\n')
#print('\nTiempo de ejecucion del bloque 3: ', tiempo_b3.tiempo(), end='\n')