#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Recibe 3 valores enteros.
Retorna el producto de los 2 primero más el 3er parámetros, usando las
funciones anteriores.
Retorna la suma de los 2 primero por el 3er parámetros, usando las
funciones anteriores.
Retorna la resta de los 2 primero por el 3er parámetros, usando las funciones
anteriores
'''

import bloque1.f_producto as producto
import bloque1.f_suma as suma
import bloque1.f_resta as resta




def p1(a,b):
    cont = True
    while cont:
        try:
            c = int(input('Ingrese un tercer valor del tipo entero: '))
            cont = False
        except ValueError:
            print('El valor ingresado no es un entero. Intente nuevamente o presione "ctrl+c".')
            cont = True
    if type(a)==int and type(b)==int and type(c)==int:      #compruebo el tipo de valores ingresados
        #res = (suma(producto(a,b),c),producto(suma(a,b),c),producto(resta(a,b),c))
        res_1 = suma.suma(producto.producto(a,b),c)
        res_2 = producto.producto(suma.suma(a,b),c)
        res_3 = producto.producto(resta.resta(a,b),c)
        res = (res_1,res_2,res_3,c)
        return res
    else:
        return('Los valores ingresados son incorrectos.')

#Prueba
#p1(1,5,7)
