import requests
import json

def sentiment_analyzer(text_to_analyse):
    # URL del servicio de análisis de sentimientos
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'

    # Construyendo la carga útil de la solicitud en el formato esperado
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Encabezado personalizado que especifica el ID del modelo para el servicio de análisis de sentimientos
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

    # Enviando una solicitud POST a la API de análisis de sentimientos
    response = requests.post(url, json=myobj, headers=header)

    # Analizando la respuesta JSON de la API
    formatted_response = json.loads(response.text)

    # Extrayendo la etiqueta de sentimiento y el puntaje de la respuesta
    label = formatted_response['documentSentiment']['label']
    score = formatted_response['documentSentiment']['score']

    # Devolviendo un diccionario que contiene los resultados del análisis de sentimientos
    return {'label': label, 'score': score}