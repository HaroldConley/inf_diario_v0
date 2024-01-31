import os
import streamlit as st
import tempfile
from orquestador import audio_a_xls
from streamlit_mic_recorder import mic_recorder


# Título WebApp
st.title('Informe Diario - Automatizado')

# Subtítulo
st.subheader('Graba un audio indicando el elemento revisado y la observación.')

audio = mic_recorder(
    start_prompt="Start recording",
    stop_prompt="Stop recording",
    just_once=False,
    use_container_width=False,
    callback=None,
    args=(),
    kwargs={},
    key=None
)


if audio:
    # st.audio(audio['bytes'])  # Muestra el reproductor del audio para escuchar la grabación

    # Crear un archivo temporal con extensión .mp3
    extension = 'mp3'
    with tempfile.NamedTemporaryFile(suffix='.' + extension, delete=False) as temp_file:
        temp_filename = temp_file.name
        temp_file.write(audio['bytes'])

    # Orquestador
    ruta_excel = r'test.xlsx'
    audio_a_xls(temp_filename, ruta_excel)

    # Elimina el archivo temporal después de usarlo
    os.remove(temp_filename)

    # Descarga el excel modificado
    with open(ruta_excel, 'rb') as excel:
        st.download_button(
            label='Descarga Informe',
            data=excel,
            file_name='Informe diario.xlsx'
        )
