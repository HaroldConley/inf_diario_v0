import whisper


def transcript(ruta_audio):
    model = whisper.load_model("base")
    result = model.transcribe(ruta_audio, language='spanish')

    return result


if __name__ == '__main__':
    ruta_audio = r"C:\Harold_DS\2024-01\02-informe_diario\02-informe_diario\audios\test.wav"
    transcripcion = transcript(ruta_audio)
    print(transcripcion['text'])
