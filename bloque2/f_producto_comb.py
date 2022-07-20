#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Función que devuelva el producto de las combinaciones posibles de los números
generados por la función genrnd tomados de a dos.

Dado que el problema posee dos posibles soluciones, ya que se 
trata de combinar números de una sola lista y que a las selecciones 
se les aplicará un producto (lo que implica que se puede obviar el 
orden de la seleccón), se desarrollan ambas:
1- Selecciones de pares sin repetición del elemento ya usado (50! / [(elemento repetido 1)!(elemento rep.2)!...] = N cantidad de Permutaciones)
2- Selecciones de pares con repetición del elemento ya usado (50 * 50 elementos = 2500 combinaciones)
Por otro lado tenemos también la posibilidad de que se quiera obviar los números ya combinados una vez:
3- Selecciones de pares sin repetición de valores (50! / [(elemento repetido 1)!(elemento rep.2)!...] = N cantidad de Permutaciones)
'''
def producto_comb1(vector):
    lista1=vector[1:]
    lista2=[]
    for i in vector:
        for j in lista1:
            lista2.append(i*j)
        lista1=lista1[1:]
    print("Cantidad de combinaciones sin repetición: " + str(len(lista2)))
    return lista2

def producto_comb2(vector):
    lista1=vector
    lista2=[]
    for i in lista1:
        for j in vector:
            lista2.append(i*j)
    print("Cantidad de combinaciones con repetición: " + str(len(lista2)))
    return lista2


def producto_comb3(vector):
    lista1=vector
    lista2=[]
    lista4=[]
    for i in lista1:
        for j in vector:
            a=(i,j)
            if a in lista2:
                break
            else:
                lista2.append(a)
                lista4.append(i*j)
    print("Cantidad de combinaciones sin repetición de cálculos: " + str(len(lista2)))
    print("Cálculos realizados: " + str(lista2))
    return lista4


# Prueba
# from f_genrnd import genrnd
# lista=genrnd()
# print(producto_comb1(lista))
# print(producto_comb2(lista))
# print(producto_comb3(lista))
# print(lista)