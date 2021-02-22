"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

import time
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import insertionsort as nsr
from DISClib.Algorithms.Sorting import selectionsort as stn
from DISClib.Algorithms.Sorting import shellsort as shr
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog(tipo: str):
    """
    Inicializa el catálogo de videos. Crea una lista vacia para guardar
    todos los videos, adicionalmente, crea una lista vacia para los paises,
    una lista vacia para las categorias y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'Videos': None,
               'Categories': None,
               }

    catalog['Videos'] = lt.newList()
    catalog['Categories'] = lt.newList()
    return catalog

# Funciones para agregar informacion al catalogo



def addCategory(catalog, category):
    """
    Adiciona una cateogría a la lista de categorías
    """
    lt.addLast(catalog['Categories'],category)



def addVideo(catalog, video,categories):

    # addVideoCategory(video, categories)
    # Se adiciona el video a la lista de videos y se le agrega su categoria correspondiente
    lt.addLast(catalog['Videos'],video)

        
    

def addVideoCategory(video, categories):
    """
    Cambia la categoria del libro con la correspondiente
    """
    # posicion = int(video['category_id'])
    # if posicion < 45:
        # nombre = lt.getElement(categories,posicion-1)
    #se añade la categoria como un campo adicional en video
        # video['Categoria'] = nombre['name']
    return None
    

# Funciones para creacion de datos


def newCountry(name):
    """
    Crea una nueva estructura para modelar los videos de
    un pais y su promedio de ratings
    """
    country = {'name': "", "videos": None}
    country['name'] = name
    country['videos'] = lt.newList('ARRAY_LIST')
    return country


def newCategory(name, id):
    """
    Esta estructura almancena los tags utilizados para marcar libros.
    """
    category = {}
    category[id] = name
    return category

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def comparecountries(countryname1, country):
    if (countryname1.lower() in country['name'].lower()):
        return 0
    return -1
    
def cmpVideosByViews(video1, video2):
    if video1['views'] < video2['views']:
        return True
    else:
        return False


def comparetagnames(name, tag):
    return (name == tag['name'])

# Funciones de ordenamiento

def sortVideos(catalogo, size, ordenamiento):
    sub_list = lt.subList(catalogo['Videos'],0,size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    if ordenamiento == 1:
        sortedlist = nsr.sort(sub_list, cmpVideosByViews)
    elif ordenamiento == 2:
        sortedlist = stn.sort(sub_list, cmpVideosByViews)
    elif ordenamiento == 3:
        sortedlist = shr.sort(sub_list, cmpVideosByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sortedlist