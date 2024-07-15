import streamlit as st
import json
import os
import zipfile
import tempfile
import nombre_jobs
import nombre_links
import nombre_rutas
import nombre_stages
import re

etiquetas = {
    "job": "job_name",
    "orchestration_flow": "job_name",
    "data_intg_flow": "link_name",
    "parameter_set": "prompt",
    "px_executables": "stages_name"
}

valores_unicos = {etiquetas[key]: set() for key in etiquetas}

def buscar_etiqueta(data, etiqueta):
    if isinstance(data, dict):
        for key, value in data.items():
            if key == etiqueta:
                yield value
            else:
                yield from buscar_etiqueta(value, etiqueta)
    elif isinstance(data, list):
        for item in data:
            yield from buscar_etiqueta(item, etiqueta)

def descomprimir_y_procesar_zip(zip_file_path, output_dir, etiqueta):
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(temp_dir)
                for root, _, files in os.walk(temp_dir):
                    for file in files:
                        if file.endswith('.osh'):
                            file_path = os.path.join(root, file)
                            procesar_archivo_osh(file_path, output_dir, etiqueta)
        st.success(f"Descompresión y procesamiento del archivo ZIP completados. Resultados guardados en '{output_dir}'.")
    except zipfile.BadZipFile:
        st.error(f"Error: El archivo '{zip_file_path}' no es un archivo ZIP válido.")
    except Exception as e:
        st.error(f"Error inesperado: {e}")

def procesar_archivo_osh(osh_file_path, output_dir, etiqueta):
    try:
        with open(osh_file_path, 'r', encoding='utf-8') as osh_file:
            for line in osh_file:
                if "STAGE:" in line:
                    stage_value = line.split("STAGE:")[1].strip()
                    valores_unicos[etiquetas[etiqueta]].add(stage_value.split(".")[0].strip())
    except FileNotFoundError:
        st.error(f"Error: El archivo OSH '{osh_file_path}' no se encontró.")
    except Exception as e:
        st.error(f"Error inesperado: {e}")

def procesar_archivo_json(file_path_json, file_json, etiqueta):
    try:
        with open(os.path.join(file_path_json, file_json), 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            if etiqueta == 'assets':
                if etiqueta in data:
                    for item in data[etiqueta]:
                        if "name" in item and "type" in item:
                            name = item["name"]
                            type_value = item["type"]
                            if type_value in ["job", "orchestration_flow"]:
                                valores_unicos[etiquetas[type_value]].add(name.split(".")[0].strip())
                            else:
                                if type_value not in ("connection", "environment"):
                                    if type_value == "px_executables":
                                        descomprimir_y_procesar_zip(os.path.join(file_path_json, f"{type_value}/{name}.zip"), name, type_value)
                                    else:
                                        buscar_y_procesar_data(file_path_json, type_value, name)
                        else:
                            st.warning(f"El objeto en '{etiqueta}' no contiene 'name' o 'type': {item}")
            else:
                for valor in buscar_etiqueta(data, etiqueta):
                    sub_folder = file_json.split("\\", 1)
                    valores_unicos[etiquetas[sub_folder[0]]].add(valor)
    except FileNotFoundError:
        st.error(f"Error: El archivo JSON '{file_path_json}' no se encontró.")
    except json.JSONDecodeError:
        st.error(f"Error: El archivo '{file_path_json}' no es un JSON válido.")
    except Exception as e:
        st.error(f"Error inesperado: {e}")

def buscar_y_procesar_data(folder_path, sub_folder, name):
    file_path = os.path.join(f"{folder_path}/{sub_folder}", f"{name}.json")
    if os.path.exists(file_path):
        procesar_archivo_json(folder_path, f"{sub_folder}/{name}.json", etiquetas[sub_folder])
    else:
        file_path = os.path.join(f"{folder_path}/{sub_folder}", f"{name}.zip")

def guardar_en_archivo(valor, archivo, output_dir):
    try:
        os.makedirs(output_dir, exist_ok=True)
        output_file_path = os.path.join(output_dir, archivo)
        with open(output_file_path, 'a', encoding='utf-8') as output_file:
            output_file.write(f"{valor}\n")
    except Exception as e:
        st.error(f"Error al guardar en el archivo '{output_file_path}': {e}")

def main(ruta):
    st.write("*************ENTRO**************")
    file_path_json = ruta
    file_json = "DataStage-README.json"
    etiqueta = 'assets'
    #ruta_salida = os.path.join(ruta, "Reporte_Insignias_CP4D.csv")
    ruta_salida = f"{ruta}\Reporte_Insignias_CP4D.csv"

    jobs = []
    links = []
    rutas = []
    stages = []

    procesar_archivo_json(file_path_json, file_json, etiqueta)

    for archivo, valores in valores_unicos.items():
        for valor in valores:
            if archivo == 'job_name':
                if re.match('SEQ_', valor) or re.match('Trial job', valor):
                    cumple_estandar = True
                    jobs.append((valor, cumple_estandar))
                else:
                    cumple_estandar = nombre_jobs.validar_nombre(valor, nombre_jobs.diccionario_T, nombre_jobs.diccionario_P)
                    jobs.append((valor, cumple_estandar))
            elif archivo == 'link_name':
                cumple_estandar = nombre_links.validar_nombre(valor, nombre_links.diccionario_L)
                links.append((valor, cumple_estandar))
            elif archivo == 'prompt':
                cumple_estandar = nombre_rutas.validar_ruta(valor, nombre_rutas.diccionario_R)
                rutas.append((valor, cumple_estandar))
            else:
                cumple_estandar = nombre_stages.validar_nombre_stage(valor, nombre_stages.diccionario_G)
                stages.append((valor, cumple_estandar))

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

    if cantidad_total == 0:
        cantidad_total = 1

    total = round((cantidad_true / cantidad_total) * 100, 2)

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

        archivo_salida.write("\nNombre Rutas:\n")
        for ruta in rutas:
            archivo_salida.write(f"{ruta}\n")
        archivo_salida.write(f"\n{total}%\n")

    st.success(f"El reporte se ha generado correctamente y se ha guardado en {ruta_salida}.")
