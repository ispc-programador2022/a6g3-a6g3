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
from f_producto import producto
from f_suma import suma
from f_resta import resta

def p1(a,b,c):
    if type(a)==int and type(b)==int and type(c)==int:      #compruebo el tipo de valores ingresados
        #res = (suma(producto(a,b),c),producto(suma(a,b),c),producto(resta(a,b),c))
        res_1 = suma(producto(a,b),c)
        res_2 = producto(suma(a,b),c)
        res_3 = producto(resta(a,b),c)
        res = (res_1,res_2,res_3)
        return res
    else:
        return('Los valores ingresados son incorrectos.')

#Prueba (no puede realizarse si las funciones f_suma, f_resta y f_producto aun no fueron escritas)
#p1(1,5,7)