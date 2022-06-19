"""1. Escribir un programa para el manejo de listas el cuál cumplirá los siguientes
requerimientos:
Reglas:
- Crear una función que le permitirá almacenar 10 número aleatorios.
- Crear una función que le permita almacenar los números no repetidos de la
lista anterior, retornar este valor e imprimir por pantalla.
- Crear una lista para ordenar de mayor a menor la lista que se creará en
ítem 2 (número no repetidos) y otra lista para ordenarlas de menor a
mayor, retornar este valor e mostrar por pantalla.
- Crear una función para indicar cuál es mayor número de la lista (lista del
ítem 2), retornar este valor e imprimirlo por pantalla."""

import random

miLista = []

for numero in range(10):
    print(numero)
    miLista.append(random.randrange(1, 100))


lista2 = miLista
if numero!=0:


print("Lista inicial es: {}".format(miLista))