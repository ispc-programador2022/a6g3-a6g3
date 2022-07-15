


import bloque1.f_producto as producto
import bloque1.f_cociente as cociente
import bloque1.f_potencia as potencia
import bloque1.f_radicacion as radicacion
import bloque1.f_suma as suma
import bloque1.f_resta as resta
import bloque1.f_presentacion as presentacion
import bloque1.f_ing2i as ing2i
import bloque1.f_ing2s as ing2s
import bloque1.f_modulo as modulo
import bloque1.f_p1 as p1


presentacion.funcionPresentacion()
enteros = ing2i.ing2i()


# print('suma: ', suma.suma(enteros[0], enteros[1]))
# print('resta: ', resta.resta(enteros[0], enteros[1]))
print('producto: ', producto.producto(enteros[0], enteros[1]))
print('cociente: ', cociente.cociente(enteros[0], enteros[1]))
print('modulo: ', modulo.modulo(enteros[0], enteros[1]))
print('potencia: ', potencia.potencia(enteros[0], enteros[1]))
print('radicacion: ', radicacion.radicacion(enteros[0], enteros[1]))

entero3 = int(input('ingrese el 3 entero: '))
print('p1: ', p1.p1(enteros[0], enteros[1], entero3))
