#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Django's command-line utility for administrative tasks."""

import random

# TODO #1a: importar  el modulo db_productos
import db_productos


def main():
    def higherandlowervalue(list):

        return (min(list), max(list))

    def averagenumberinlist(list):
        return sum(list) / len(list)

    def countnumbers(list, chosenNumber):
        count = 0
        for number in list:
            if chosenNumber < number:
                count += 1
        return count

    # TODO #2: definir una función mostrar_productos()
    #          que reciba la lista de productos, no retorne nada,
    #          y muestre la lista utilizando el siguiente formato para cada producto:

    # "Producto {id}"
    # "{nombre} ${precio}"
    # "---"
    # "Producto {id}"
    # "{nombre} ${precio}"
    # "---"
    # ...

    def mostrarProducto(list):
        for producto in list:
            print(f'Producto {producto["id"]}')
            print(f'{producto["nombre"]}, ${producto["precio"]}')

    # TODO #3: definir una función calcular_precio_actualizado()
    #          que reciba: el precio anterior y porcentaje de aumento
    #          y retorne: el precio con el aumento.

    def calcular_precio_actualizado(precio, porcentaje):
        return precio + (porcentaje * precio / 100)

    # TODO #4: Crear una función actualizar_precios() que reciba la lista de productos y
    #          el porcentaje de aumento. La función debe recorrer cada producto de la
    #          lista e invocar calcular_precio_actualizado() (a la cual tendrá que pasarle
    #          el precio del producto y el porcentaje de aumento) para obtener el precio
    #          actualizado y modifique la lista "in-place" actualizando el precio de cada
    #          producto. La función no debe retornar nada sino dejar modificada la lista
    #          pasada por el usuario.

    def actualizar_precios(productos, porcentaje_de_aumentos):
        for producto in productos:
            producto["precio"] = calcular_precio_actualizado(
                producto["precio"], porcentaje_de_aumentos
            )
        print("Precios actualizados: ")
        mostrarProducto(productos)

    def generar_lista_de_atletas():
        """
        Esta función genera aleatoriamente los datos de 20 atletas que participaron de una maratón.
        Devuelve una lista de atletas donde cada atleta es un diccionario con los campos:
            - nombre: el nombre del atleta
            - numero: el número con el que participó en la maratón
            - tiempo_llegada: la cantidad de segundos que tardó en llegar
        """
        lista_atletas = []
        nombres = (
            "Daniel",
            "Alejandro",
            "Pablo",
            "Hugo",
            "Álvaro",
            "Adrián",
            "David",
            "Sergio",
            "Diego",
        )
        apellidos = (
            "García",
            "Rodríguez",
            "González",
            "Fernández",
            "López",
            "Martínez",
            "Sanchez",
            "Pérez",
        )
        for i in range(1, 21):
            atleta = {
                "nombre": random.choice(nombres) + " " + random.choice(apellidos),
                "numero": i,
                "tiempo_llegada": random.random() * 120,
            }
            lista_atletas.append(atleta)
        return lista_atletas

    def imprimir_lista_de_atletas(lista_de_atletas):
        for atleta in lista_de_atletas:
            print(
                f'{atleta["numero"]}, {atleta["nombre"]} - : ({atleta["tiempo_llegada"]} segundos)'
            )

    def numero_atleta_ganador(lista_de_atletas):
        atleta_ganador = lista_de_atletas[0]
        for atleta in lista_de_atletas:
            if atleta_ganador["tiempo_llegada"] > atleta["tiempo_llegada"]:
                atleta_ganador = atleta

        return atleta_ganador["numero"]

    def get_atleta(numero_atleta, lista_de_atletas):
        for atleta in lista_de_atletas:
            if atleta["numero"] == numero_atleta:
                return atleta

    def podio(lista_de_atletas):
        tupla = ()
        for i in range(3):
            numero = numero_atleta_ganador(lista_de_atletas)
            atleta = get_atleta(numero, lista_de_atletas)
            tupla = tupla + (atleta,)
            lista_de_atletas.remove(atleta)
        return tupla

    def ejercicio1():
        list = []

        for i in range(9):
            randomNumber = random.randint(1, 20)
            list.append(randomNumber)
        print(f"Lista {list}")
        chosenNumber = int(input("Ingrese un valor de la lista: "))
        if chosenNumber in list:
            response = countnumbers(list, chosenNumber)
            print(f"La cantidad de numeros mayores al elegido son: {response}")
        else:
            print("El numero elegido no se encuentra en la lista")
        print(f"El valor promedio de la lista es: {averagenumberinlist(list)}")
        (minimo, maximo) = higherandlowervalue(list)
        print(f"el maximo es: {maximo} y el minimo: {minimo}")

    def ejercicio2():

        # TODO #1b: cargar la lista de productos con la función
        #          cargar_productos() del módulo db_productos.
        productos = db_productos.cargar_productos()

        # TODO #5a: mostrar la lista cargada
        # TODO #5b: el usuario debe ingresar el porcentaje de aumento
        # TODO #5c: usar la función actualizar_precios() para actualizar los precios de la lista
        # TODO #5d: mostrar la lista con los precios actualizados
        mostrarProducto(productos)

        porcentaje_de_aumentos = float(input("Ingrese porcentaje de aumento: "))
        actualizar_precios(productos, porcentaje_de_aumentos)

    def ejercicio3():
        lista_de_atletas = generar_lista_de_atletas()
        imprimir_lista_de_atletas(lista_de_atletas)
        numero_ganador = numero_atleta_ganador(lista_de_atletas)
        print(("-------------------------"))
        print(f"Numero de atleta ganador : {numero_ganador}")
        print(("-------------------------"))
        numero_atleta = int(input("Ingrese numero de atleta: "))
        atleta = get_atleta(numero_atleta, lista_de_atletas)
        print(
            f'{atleta["numero"]}, {atleta["nombre"]} - : ({atleta["tiempo_llegada"]} segundos)'
        )
        print(("-------------------------"))
        tupla = podio(lista_de_atletas)
        print(("Podio: "))
        print(tupla)

    ejercicio = int(input("Ingrese ejercicio: "))

    if ejercicio == 1:
        ejercicio1()
    elif ejercicio == 2:
        ejercicio2()
    elif ejercicio == 3:
        ejercicio3()
    else:
        print("Numero de ejercicio incorrecto. Fin del programa.")


if __name__ == "__main__":
    main()
