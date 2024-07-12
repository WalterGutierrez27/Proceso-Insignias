import streamlit as st
import os
from main import Procesador
import CP4D_wr as cp4d

# Definir la ruta base de descargas
ruta_base_descargas = os.path.join(os.path.expanduser("~"), "Downloads")

# Establecer el color de fondo para la parte central y barras negras a los lados
st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFFFFF; /* Fondo blanco */
    }
    .main {
        background-color: #FFFFFF;
        padding: 20px;
        border-left: 10px solid #000000; /* Barra negra izquierda */
        border-right: 10px solid #000000; /* Barra negra derecha */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Establecer Fondo para la barra izq
st.markdown(
    """
    <style>
    blockquote {
        background-color: #FFFFFF; /* Fondo blanco */
        color: black; /* Letras negras */
    }
    blockquote p {
        font-size: 30px;
        color: black; /* Letras negras */
    }
    [data-testid="stSidebar"] {
        background-color: rgb(0, 0, 0); /* Color de fondo original */
        color: #FFFFFF; /* Color de letras original (blanco) */
    }
    [aria-selected="true"] {
        color: black; /* Letras negras */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Estilo para la imagen y el título
estilo_imagen = """
    <style>
    .imagen {
        display: inline-block;
        vertical-align: middle;
    }
    .titulo {
        color: red;
        display: inline-block;
        vertical-align: middle;
        margin-left: 10px;
        margin-top: 0;
    }
    </style>
    """
st.markdown(estilo_imagen, unsafe_allow_html=True)

# Contenedor principal
col1, col2 = st.columns([1, 2])

# Imagen
col1.image(os.path.join("LogoSetiAio.jpg"), caption='', width=100, use_column_width=True)

# Título
col2.markdown("<h1 class='titulo'>Proceso Insignias Estandares Desarrollo </h1>", unsafe_allow_html=True)

# Barra lateral (sidebar)
# Cargar la imagen en el sidebar y alinearla a la derecha
st.sidebar.image(os.path.join("descargar.jfif"), caption='Insignias', width=100, use_column_width=True)

# Opciones de proyectos y selección en el sidebar
st.sidebar.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Crear una instancia del procesador
procesador = Procesador()

with st.sidebar:
    project_options = ['proyecto_bogota', 'proyecto_popular', 'CP4D']
    selected_project = st.selectbox("Selecciona un proyecto", project_options)

if selected_project == 'CP4D':
    with st.sidebar:
        ruta = st.text_input("Introduce la ruta del folder a procesar")

    # Estilo personalizado para botones
    st.markdown(
        """
        <style>
        div.stButton > button {
            background-color: #000000;
            border: none;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 12px;
        }

        div.stDownloadButton > button {
            background-color: #000000;
            border: none;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 12px;
        }
        .stSuccess, .stError, .stWarning, .stInfo {
            color: #000000; /* Cambia esto por el color que prefieras */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    if st.button("Procesar archivo"):
        if ruta:
            ruta = ruta.strip()  # Eliminar espacios en blanco
            if os.path.exists(ruta) and os.path.isdir(ruta):
                st.markdown(
                    """
                    <div style="background-color: #000000; color: white; padding: 10px; border-radius: 5px;">
                        El reporte se generó satisfactoriamente, si deseas mayor detalle, ¡pulsa el botón descargar!
                    </div>
                    <br>
                    """,
                    unsafe_allow_html=True
                )
                try:
                    cp4d.main(ruta)
                    #ruta_salida = os.path.join(ruta, "Reporte_Insignias_CP4D.csv")
                    ruta_salida = os.path.join(ruta, "prueba", "Reporte_Insignias_CP4D.csv")
                    st.write(ruta_salida)
                    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)

                    if os.path.exists(ruta_salida):
                        with open(ruta_salida, 'r', encoding='latin-1') as file:
                            lines = file.readlines()

                        if len(lines) >= 2:
                            penultima_linea = lines[-1].strip()
                            st.markdown(
                                f"""
                                <div style="background-color: #000000; color: white; padding: 10px; border-radius: 5px;">
                                    El porcentaje de cumplimiento del proyecto {selected_project} es: {penultima_linea}
                                </div>
                                <br>
                                """,
                                unsafe_allow_html=True
                            )
                        else:
                            st.warning("El archivo no tiene suficientes líneas para mostrar la penúltima línea.")

                        with open(ruta_salida, 'rb') as file:
                            file_data = file.read()

                        st.download_button(
                            label="Descargar reporte",
                            data=file_data,
                            file_name="Reporte_Insignias_CP4D.csv",
                            mime="text/csv"
                        )
                    else:
                        st.error(f"No se encontró el archivo en la ruta especificada: {ruta_salida}")

                except PermissionError:
                    st.error("Permiso denegado para acceder a esta ruta.")
                except Exception as e:
                    st.error(f"Error al listar la ruta: {e}")
            else:
                st.error("La ruta introducida no existe o no es un directorio.")
        else:
            st.warning("Por favor, introduce una ruta.")
else:
    custom_css = """
    <style>
        .stFileUploader label div:first-child {
            font-size: 1rem;
            color: #F1C40F;
        }
        .stFileUploader label div:first-child:before {
            content: 'Arrastra y suelta tu archivo aquí o haz clic para buscar';
            display: block;
        }
        .stFileUploader label div:first-child span {
            display: none;
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    with st.sidebar:
        uploaded_file = st.file_uploader("Selecciona un archivo .dsx para procesar", type="dsx")

    st.markdown(
        """
        <style>
        div.stButton > button {
            background-color: #000000;
            border: none;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 12px;
        }

        div.stDownloadButton > button {
            background-color: #000000;
            border: none;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 12px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    if st.button("Procesar archivo"):
        if uploaded_file is not None:
            try:
                contenido_archivo = [line.decode('latin-1').strip() for line in uploaded_file]
                ruta_salida = os.path.join(ruta_base_descargas, f"Reporte_Insignias_{selected_project}.csv")
                os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
                
                procesador.main(contenido_archivo, selected_project, ruta_salida)
                st.markdown(
                    """
                    <div style="background-color: #000000; color: white; padding: 10px; border-radius: 15px;">
                        El reporte se generó satisfactoriamente, si deseas mayor detalle, ¡pulsa el botón descargar!
                    </div>
                    <br>
                    """,
                    unsafe_allow_html=True
                )

                with open(ruta_salida, 'r', encoding='latin-1') as file:
                    lines = file.readlines()

                if len(lines) >= 2:
                    penultima_linea = lines[-1].strip()
                    st.markdown(
                        f"""
                        <div style="background-color: #000000; color: white; padding: 10px; border-radius: 15px;">
                            El porcentaje de cumplimiento del {selected_project} es: {penultima_linea}
                        </div>
                        <br>
                        """,
                        unsafe_allow_html=True
                    )
                else:
                    st.warning("El archivo no tiene resultados por mostrar")

                with open(ruta_salida, 'rb') as file:
                    file_data = file.read()

                st.download_button(
                    label="Descargar reporte",
                    data=file_data,
                    file_name=f"Reporte_Insignias_{selected_project}.csv",
                    mime="text/csv"
                )

            except UnicodeDecodeError:
                st.error("Error al decodificar el archivo.")
        else:
            st.error("Por favor, sube un archivo y selecciona un proyecto.")
