#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Función que calcule la varianza del vector obtenido en genrnd.

La Varianza es una medida de dispersión que se utiliza para representar 
la variabilidad de un conjunto de datos respecto de la media aritmética 
de los mismo. Así, se calcula como la suma de los residuos 
elevados al cuadrado y divididos entre el total de observaciones.
'''



from bloque2.f_media import media


def varianza(vector):
    med = media(vector)
    l_restos = []
    for i in vector:               
        nume = (i - med)**2
        l_restos.append(nume)       #armo una lista con las diferencias entre los valores del vector y la media, elevadas al cuadrado
    total_restos = sum(l_restos)
    return total_restos/len(vector) #(total_restos/len(vector))**(1/2) desviación típica

#Test
#from f_genrnd import genrnd
#print(varianza(genrnd()))