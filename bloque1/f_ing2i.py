#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Pide el ingreso por teclado de 2 enteros.
Retorna los enteros en una lista de 2 elementos.
'''

def ing2i():
    #print("Funcion ing2i:")
    cont = True
    while cont:
        try:
            a=int(input("Ingrese el primer entero: "))
            b=int(input("Ingrese el segundo entero: "))
            cont = False
        except TypeError:
            print('TypeError: Falló la función, inténtelo nuevamente')
            #return
        except ValueError:
            print('ValueError: Falló la función, inténtelo nuevamente')
            #return 
    return [a,b]

#Prueba:
#ing2i()
