import json
import os
from openai import OpenAI


def data_extraction(api_key, transcripcion):
    # Inicializando el cliente de OpenAI
    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        temperature=0,
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """
            Te voy a entregar la transcripción de un audio de un inspector de obra que está revisando el estado de un elemento.
            Necesito que identifiques el elemento inspeccionado y la observación hecha. 
            La observación deber ser muy concisa, solo indicando lo que se observa, no acciones, causas ni efectos.
            La respuesta debe ser con este formato, y en JSON:
    
            "
            elemento:
            observacion:
            "
            """},
            {"role": "user", "content": f"""{transcripcion}"""}
            ]
        )

    response_dict = json.loads(response.choices[0].message.content)

    return response_dict


if __name__ == '__main__':
    api_key=os.environ['OPENAI_API_KEY']
    transcripcion = """
            ' Estamos revisando los asensores y se observa que aún se mantienen las filtraciones activas.'"""

    response_dict = data_extraction(api_key, transcripcion)
    print(response_dict['elemento'])
    print(response_dict['observacion'])
