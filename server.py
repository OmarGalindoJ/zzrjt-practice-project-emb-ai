from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    # Recupera el texto a analizar de los argumentos de la solicitud
    text_to_analyze = request.args.get('textToAnalyze')

    # Pasa el texto a la función sentiment_analyzer y almacena la respuesta
    response = sentiment_analyzer(text_to_analyze)

    # Extrae la etiqueta y la puntuación de la respuesta
    label = response['label']
    score = response['score']

   # Verifica si el label es None, indicando un error o entrada no válida
    if label is None:
        return "¡Entrada no válida! Intenta de nuevo."
    else:
        # Devuelve una cadena formateada con el label de sentimiento y el score
        return "El texto dado ha sido identificado como {} con un score de {}.".format(label.split('_')[1], score)

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
