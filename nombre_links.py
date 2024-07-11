import re
import diccionarios

diccionario_L = diccionarios.get_l()

def verificar_patron(cadena, patron):
    busqueda = re.search(patron, cadena)
    if busqueda:
        return True
    else:
        return False
    
def buscar_links(palabra, archivo, arreglo):
    for i, linea in enumerate(archivo):
        if palabra in linea:
            if i + 1 < len(archivo):
                siguiente_linea = archivo[i]
                arreglo.append(siguiente_linea[11:-1])

def validar_nombre(cadena, diccionario_L):
    for L in diccionario_L.keys():
        patron = r'^{}_.*'.format(re.escape(L))
        componente = verificar_patron(cadena, patron)
        if componente:
            return True
    return False

def ejecutar_nombre_links(archivo):
    nombre_links = []
    estandar_links = []
    busqueda_links = "LinkNames"
    buscar_links(busqueda_links, archivo, nombre_links)

    caracteres_reemplazar = [' ', '|', ',']
    for palabra in range(len(nombre_links)):
        for caracter in caracteres_reemplazar:
            nombre_links[palabra] = nombre_links[palabra].replace(caracter, ' ')

    for elemento in nombre_links:
        links = elemento.split()
        for nombre in links:
            estandar_links.append(nombre.strip())

    resultados = []
    for nombre in estandar_links:
        cumple_estandar = validar_nombre(nombre, diccionario_L)
        resultados.append((nombre, cumple_estandar))
    return resultados
