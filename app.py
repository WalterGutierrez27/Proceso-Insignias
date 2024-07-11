import streamlit as st
import os
from main import Procesador
import CP4D_wr as cp4d

# Definir la ruta base como un parámetro
ruta_base = "C:/Users/waltergutierrez/"

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
#col1.image(os.path.join(ruta_base, "OneDrive - SETI S.A.S/SETI/OKRS 2024/Desarrollo Insignias Python/Python/Entrada/Imagenes/LogoSetiAio.jpg"), caption='', width=100, use_column_width=True)
col1.image(os.path.join(LogoSetiAio.jpg), caption='', width=100, use_column_width=True)

# Título
col2.markdown("<h1 class='titulo'>Proceso Insignias Estandares Desarrollo </h1>", unsafe_allow_html=True)


            except UnicodeDecodeError:
                st.error("Error al decodificar el archivo.")
        else:
            st.error("Por favor, sube un archivo y selecciona un proyecto.")
