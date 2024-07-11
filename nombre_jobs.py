import re
import diccionarios
from itertools import product

diccionario_P = diccionarios.get_p()
diccionario_T = diccionarios.get_t()

def verificar_patron(cadena, patron):
    busqueda = re.search(patron, cadena)
    if busqueda:
        return True
    else:
        return False

def buscar_nombre_job(palabra, archivo, arreglo):
    for i, linea in enumerate(archivo):
        if palabra in linea:
            if i + 1 < len(archivo):
                siguiente_linea = archivo[i + 1]
                arreglo.append(siguiente_linea[12:-1])

def validar_nombre(cadena, diccionario_T, diccionario_P):
    for T, P in product(diccionario_T.keys(), diccionario_P.keys()):
        patron = r'^{}_{}_.*'.format(re.escape(T), re.escape(P))
        componente = verificar_patron(cadena, patron)
        if componente:
            return True
    return False

def ejecutar_nombre_jobs(archivo):
    nombre_jobs = []
    busqueda = "BEGIN DSJOB"
    buscar_nombre_job(busqueda, archivo, nombre_jobs)

    resultados = []
    for nombre in nombre_jobs:
        if "SEQ_" in nombre:
            cumple_estandar = True
        else:
            cumple_estandar = validar_nombre(nombre, diccionario_T, diccionario_P)
        resultados.append((nombre, cumple_estandar))
    return resultados
