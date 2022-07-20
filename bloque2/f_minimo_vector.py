#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def minimo_del_vector(vector):
    
    menor =vector [0] 
    
    for n in range(1, len (vector)) :
        if vector [n] < menor:
            menor= vector [n]
    return menor
