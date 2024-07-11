import diccionarios
import nombre_jobs
import nombre_stages
import nombre_links
import nombre_rutas

class Procesador:
    def __init__(self):
        self.proyecto_bogota = diccionarios.get_bogota()
        self.proyecto_popular = diccionarios.get_popular()

    def main(self, contenido_archivo, value, ruta_salida):
        def seleccionar_diccionario(value):
            if value == 'proyecto_bogota':
                return self.proyecto_bogota.keys()
            elif value == 'proyecto_popular':
                return self.proyecto_popular.keys()
            else:
                return {}

        def extraer_contenido(lista):
            # Asegurarse de que la lista no esté vacía
            if lista:
                return lista[0]
            else:
                return None

        resultado = extraer_contenido(list(seleccionar_diccionario(value)))
        busqueda_rutas1 = resultado
        busqueda_rutas2 = 'ParamValues'

        def consolidar_informacion():
            jobs = nombre_jobs.ejecutar_nombre_jobs(contenido_archivo)
            stages = nombre_stages.ejecutar_stages(contenido_archivo)
            links = nombre_links.ejecutar_nombre_links(contenido_archivo)
            rutas = nombre_rutas.ejecutar_nombre_rutas(contenido_archivo, busqueda_rutas1, busqueda_rutas2)

            cantidad_jobs_true = sum(1 for _, valor in jobs if valor is True)
            cantidad_stages_true = sum(1 for _, valor in stages if valor is True)
            cantidad_links_true = sum(1 for _, valor in links if valor is True)
            cantidad_rutas_true = sum(1 for _, valor in rutas if valor is True)

            cantidad_jobs = len(jobs)
            cantidad_stages = len(stages)
            cantidad_links = len(links)
            cantidad_rutas = len(rutas)

            cantidad_total = cantidad_jobs + cantidad_stages + cantidad_links + cantidad_rutas
            cantidad_true = cantidad_jobs_true + cantidad_stages_true + cantidad_links_true + cantidad_rutas_true
            total = round((cantidad_true / cantidad_total) * 100, 2)

            return jobs, stages, links, rutas, total

        jobs, stages, links, rutas, total = consolidar_informacion()

        with open(ruta_salida, "w") as archivo_salida:
            archivo_salida.write("Nombres Jobs:\n")
            for job in jobs:
                archivo_salida.write(f"{job}\n")

            archivo_salida.write("\nNombres Stages:\n")
            for stage in stages:
                archivo_salida.write(f"{stage}\n")

            archivo_salida.write("\nNombres Links:\n")
            for link in links:
                archivo_salida.write(f"{link}\n")

            archivo_salida.write("\nNombres Rutas:\n")
            for ruta in rutas:
                archivo_salida.write(f"{ruta}\n")

            archivo_salida.write(f"\n{total}%\n")
