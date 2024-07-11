import re
import diccionarios

diccionario_R = diccionarios.get_r()

def verificar_patron(cadena, patron):
    busqueda = re.search(patron, cadena)
    if busqueda:
        return True
    else:
        return False

def validar_ruta(arreglo, diccionario_R):
    for R in diccionario_R.keys():
        patron = r'^{}'.format(re.escape(R))
        componente = verificar_patron(arreglo, patron)
        if componente:
            return True
    return False

def ejecutar_nombre_rutas(archivo, rutas1, rutas2):
    nombre_rutas1 = []
    nombre_rutas2 = []

    def buscar_rutas_palabra1(palabra, arreglo):
        lines = arreglo
        inicio = False
        for line in lines:
            if inicio:
                nombre_rutas1.append(line)
            if palabra in line:
                inicio = True

    def buscar_rutas_palabra2(palabra, arreglo):
        for i, linea in enumerate(arreglo):
            if palabra in linea:
                if i + 1 < len(arreglo):
                    siguiente_linea = arreglo[i]
                    nombre_rutas2.append(siguiente_linea[:-1])

    buscar_rutas_palabra1(rutas1, archivo)
    buscar_rutas_palabra2(rutas2, nombre_rutas1)

    def extraer_palabras(texto):
        palabras = re.findall(r'\bS\$\w+', texto)
        return palabras

    cadena_texto = ' '.join(nombre_rutas2)
    arreglo_palabras = extraer_palabras(cadena_texto)

    caracteres_reemplazar = ['S$', ' ']
    for palabra in range(len(arreglo_palabras)):
        for caracter in caracteres_reemplazar:
            arreglo_palabras[palabra] = arreglo_palabras[palabra].replace(caracter, '')

    resultados = []
    for nombre in arreglo_palabras:
        cumple_estandar = validar_ruta(nombre, diccionario_R)
        resultados.append((nombre, cumple_estandar))
    resultados = list(set(resultados))
    return resultados
