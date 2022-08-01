

""" Retorna una lista con 500.000.000.000.000.000 números aleatorios. 

5*10^17
"""

import random

def barra_progreso(progreso, total):
    porcentage=100*(progreso/float(total))
    barra=('|'*int(porcentage) + '-'*(100-int(porcentage)))
    print(f"\r|{barra}| {porcentage:.2f}%",end="\r")

def genrnd():
    print("Calculando nùmeros 500.000.000.000.000.000 aleatorios:")
    lista_rnd = []
    for i in range(5*10**17):
        lista_rnd.append(random.randint(0,1000))
        if i%(5*10**13)==0:
            barra_progreso(i+1, 5*10**17)
    return lista_rnd

#Test
print(genrnd())
