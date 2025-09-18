import requests
import json

def sentiment_analyzer(text_to_analyse):
    # Define la URL para la API de análisis de sentimientos
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    
    # Crea la carga útil con el texto a analizar
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # Establece los encabezados con el ID de modelo requerido para la API
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    
    # Realiza una solicitud POST a la API con la carga útil y los encabezados
    response = requests.post(url, json=myobj, headers=header)
    
    # Analiza la respuesta de la API
    formatted_response = json.loads(response.text)
    
    # Si el código de estado de la respuesta es 200, extrae el label y el score de la respuesta
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']    # Si el código de estado de la respuesta es 500, establece label y score en None
    elif response.status_code == 500:
        label = None
        score = None
    
    # Devuelve el label y el score en un diccionario
    return {'label': label, 'score': score}