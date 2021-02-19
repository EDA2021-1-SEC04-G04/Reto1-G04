"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
import time
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Consultar los videos de una categoría más vistos en un país")
    print("3- Conocer el video que más días ha sido trending en un país")
    print("4- Averiguar el video que más días ha sido trending en una categoría")
    print("5- Consultar los n videos con un tag específico que más likes han tenido en un país")
    print("0- Salir")

def initCatalog():
    """
    Inicializa el catalogo de videos
    """
    return controller.initCatalog()

def loadData(catalog):
    """
    Carga los videos en la estructura de datos
    """
    controller.loadData(catalog)

def imprimir_primer_elemento(catalog):
    elementos_pais = catalog['elements'][0]['videos']['elements'][0]
    print(elementos_pais)

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Selecci1one una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        t1 = time.time_ns()
        catalog = initCatalog()
        loadData(catalog)
        t2 = time.time_ns()
        print('El tiempo de carga fue de ' , ((t2-t1)/1000000))
        print('Videos cargados: ' + str(lt.size(catalog['Videos'])))
        print('Paises cargados: ' + str(lt.size(catalog['Country'])))
        print('Categorias cargadas: ' + str(lt.size(catalog['Categories'])))
        print('Asociación de Categorías a Videos cargados: ' +
              str(lt.size(catalog['Videos'])))

    elif int(inputs[0]) == 2:
        imprimir_primer_elemento(catalog['Country'])

    else:
        sys.exit(0)
sys.exit(0)
