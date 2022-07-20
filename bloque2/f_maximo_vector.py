#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def maximo_del_vector(vector):
    
    mayor =vector [0] 
    
    for n in range(1, len (vector)) :
        if vector [n] > mayor:
            mayor= vector [n]
    return mayor 
