#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Funcion que genera una presentacion del trabajo de grupo.
'''
o="@"
v=" "

""" 
toma una tupla y un booleano
Función utilizada para armar los renglones del cartel
devuelve un string con salto de línea al final
"""
def armorengl(tup,ban):
    # Armo renglón
    for x in tup:
        if ban:
            print(v*x*3,end="")
            ban=False
        else:
            print(o*x*3,end="")
            ban=True
    print("\n")

""" 
Función que muestra un cartel a modo de presentación 
"""
def funcionPresentacion():
    prim=(1,2,4,1,3,3,1,7)
    seg=(1,2,1,2,1,3,1,5,1,1,1,1,1)
    ter=(1,2,1,1,1,4,1,5,1,1,1,1,1)
    cuar=(4,1,3,2,1,1,2,2,1,1,1,1,1)
    quin=(1,2,1,1,2,1,1,1,2,1,2,1,1,1,1,1,1)
    sex=(1,2,1,2,2,3,3,1,7)
    oct=(22,)

    armorengl(prim,True)
    armorengl(seg,False)
    armorengl(ter,False)
    armorengl(cuar,False)
    armorengl(quin,False)
    armorengl(sex,False)
    armorengl(oct,False)
 
#Prueba:    
#funcionPresentacion()