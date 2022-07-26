#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Función que devuelva el cociente de las combinaciones posibles de los números
generados por la función genrnd tomados de a dos.
'''
def cociente(dividendo, divisor):
    if ( dividendo < divisor):
        return 0;
    else:
        return 1 + cociente(dividendo-divisor, divisor);

#dividendo = int(input("\ningresar dividendo: "))
#divisor = int(input("\n ingresar divisor: "))
#print("cociente de dos numeros: " +str(cociente(dividendo, divisor)))