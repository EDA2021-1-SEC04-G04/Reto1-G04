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


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de videos. Crea una lista vacia para guardar
    todos los videos, adicionalmente, crea una lista vacia para los paises,
    una lista vacia para las categorias y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'Videos': None,
               'Country': None,
               'Categories': None,
               'Videos_Categories': None}

    catalog['Videos'] = lt.newList()
    catalog['Country'] = lt.newList('ARRAY_LIST',
                                    cmpfunction=comparecountries)
    catalog['Categories'] = lt.newList('ARRAY_LIST',
                                 cmpfunction=comparetagnames)
    catalog['Video_Categories'] = lt.newList('ARRAY_LIST')
    return catalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    # Se adiciona el video a la lista de videos y se le agrega su categoria correspondiente
    categories = catalog['Categories']
    category = addVideoCategory(video['category_id'],categories['elements'])
    video['category'] = category
    lt.addLast(catalog['Videos'], video)
    # Se obtienen el canal del video
    countries = video['country'].split(",")
    # Cada canal, se crea en la lista de videos del catalogo, y se
    # crea un video en la lista de dicho canal (apuntador al video)
    for country in countries:
        addVideoCountry(catalog, country.strip(), video)
        
def addVideoCountry(catalog, country, video):
    """
    Adiciona un país a lista de países, la cual guarda referencias
    a los videos de dicho país
    """
    countries = catalog['Country']
    poscountry = lt.isPresent(countries, country)
    if poscountry > 0:
        country = lt.getElement(countries, poscountry)
    else:
        country = newCountry(country)
        lt.addLast(countries, country)
    lt.addLast(country['videos'], video)

def addCategory(catalog, category):
    """
    Adiciona una cateogría a la lista de categorías
    """
    for valor in category:
        cont = 0
        while cont <1:
            cat = category['id\tname'].split("\t",1)
            cont +=1
        t = newCategory(cat[1], int(cat[0]))
    lt.addLast(catalog['Categories'], t)

def addVideoCategory(category_id, categories):
    """
    Cambia la categoria del libro con la correspondiente
    """
    new_category = None
    found = False
    ticker = 0
    while found == False and ticker <len(categories):
        for ide in categories[ticker]:
            if ide == int(category_id):
                new_category = categories[ticker][ide]
                found == True
        ticker +=1
    return new_category

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
    
def compareratings(book1, book2):
    return (float(book1['average_rating']) > float(book2['average_rating']))


def comparetagnames(name, tag):
    return (name == tag['name'])

# Funciones de ordenamiento

