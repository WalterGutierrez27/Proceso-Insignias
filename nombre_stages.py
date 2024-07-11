import re
import diccionarios

diccionario_G = diccionarios.get_g()

busqueda_stages = "StageNames"
busqueda_tipo_stages = "StageTypeIDs"

def verificar_patron(cadena, patron):
    return bool(re.search(patron, cadena))

def validar_nombre_stage(nombre, diccionario_G):
    for G in diccionario_G.keys():
        patron = r'^{}_.*'.format(re.escape(G))
        if verificar_patron(nombre, patron):
            return True
    return False

def ejecutar_stages(archivo):

    nombre_stages = []
    tipo_stages = []
    estandar_stages = []

    def buscar_palabra(palabra, entrada, salida, posicion):
        for linea in entrada:
            if palabra in linea:
                salida.append(linea[posicion:].strip())

    def limpieza_arreglo(arreglo):
        caracteres_reemplazar = [', ', '|', ',', '"']
        for i in range(len(arreglo)):
            for caracter in caracteres_reemplazar:
                arreglo[i] = arreglo[i].replace(caracter, ' ')
        return arreglo

    def arreglo_final(arreglo):
        resultado = []
        for elemento in arreglo:
            partes = elemento.split()
            for parte in partes:
                resultado.append(parte.strip())
        return resultado

    buscar_palabra(busqueda_stages, archivo, nombre_stages, 12)
    buscar_palabra(busqueda_tipo_stages, archivo, tipo_stages, 14)
    nombre_stages = limpieza_arreglo(nombre_stages)
    estandar_stages = arreglo_final(nombre_stages)

    def comparacion_nombre_stages():
        resultados = []
        for nombre in estandar_stages:
            cumple_nombre = validar_nombre_stage(nombre, diccionario_G)
            resultados.append((nombre, cumple_nombre))
        return resultados

    resultados_nombre = comparacion_nombre_stages()
    return resultados_nombre
