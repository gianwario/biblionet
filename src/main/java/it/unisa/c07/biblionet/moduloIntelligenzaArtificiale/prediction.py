import pickle
import pandas as pd
import flask
from flask import jsonify, request

# Flask permette di trattare script Python come Web Service
# In questo caso, mette a disposizione i servizi delle funzioni
# in questo file con un mapping all'indirizzo localhost:5000
app = flask.Flask(__name__)
app.config["DEBUG"] = True


# Funzione per leggere il modello già allenato da un file
def readModel():
    read_file = open('model.obj', 'rb')
    model = pickle.load(read_file)
    return model


def makePrediction(ans1, ans2, ans3, ans4, ans5):
    # Chiamo la funzione che legge il modello da file
    model = readModel()

    # Creo un dict contenente le 5 risposte dell'utente
    answers = {ans1, ans2, ans3, ans4, ans5}

    # Creo una lista che userò per memorizzare le predizioni del modello
    predictions = []

    # probabilities = []
    # i = 0

    # Effettuo un ciclo sulle risposte dell'utente e per ognuna
    # effettuo la predizione, salvandola nella lista
    for answer in answers:
        predictions.append(
            model.predict(pd.DataFrame({'answer': [answer]}))
        )
        # prediction_frame = pd.DataFrame(predictions[i])
        # data_frame = pd.DataFrame({'char1': [prediction_frame.loc[0, 'char1']],
        #                            'char2': [prediction_frame.loc[0, 'char2']],
        #                            'char3': [prediction_frame.loc[0, 'char3']],
        #                            'answer': [answer]})
        # probabilities.append(
        #     model.predict_probability(data_frame)
        # )
        # i += 1

    # Itero 5 volte, quante sono le predizioni, e per ognuna formatto
    # la risposta in una lista, in quanto il metodo model.predict() restituisce
    # un formato diverso da quello che serve. Restituisco la lista di generi
    results = []
    for j in range(0, 5):
        tmp = pd.DataFrame(predictions[j])
        results.append(tmp.loc[0, 'genre'])

    return results


# Questo metodo si occupa di ricevere una chiamata HTTP, in particolare
# una POST, all'indirizzo localhost:5000/
# Riceve un JSON contenente le 5 risposte dell'utente, chiama il metodo prediction
# e restituisce la lista di generi restituiti sottoforma di JSON
@app.route('/', methods=['POST'])
def home():

    json = request.json
    return jsonify(makePrediction(json['ans1'], json['ans2'], json['ans3'], json['ans4'], json['ans5']))


app.run()

