from src.audio_transcript.audio_transcript import transcript
from src.data_extraction.data_extraction import data_extraction
from src.excel_fill.excel_fill import escribir_celda_excel


def audio_a_xls(ruta_audio, ruta_excel):
    api_key = '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'

    transcripcion = transcript(ruta_audio=ruta_audio)
    datos_dict = data_extraction(api_key, transcripcion['text'])

    hoja = '22-09-2021'
    celda = 'H3'
    valor = datos_dict['elemento']
    escribir_celda_excel(ruta_excel, hoja, celda, valor)

    hoja = '22-09-2021'
    celda = 'I3'
    valor = datos_dict['observacion']
    escribir_celda_excel(ruta_excel, hoja, celda, valor)


if __name__ == '__main__':
    ruta_audio = r"C:\Harold_DS\2024-01\02-informe_diario\02-informe_diario\audios\test_ascensor.ogg"
    ruta_excel = r'C:\Harold_DS\2024-01\02-informe_diario\02-informe_diario\src\excel_fill\test.xlsx'

    audio_a_xls(ruta_audio, ruta_excel)
