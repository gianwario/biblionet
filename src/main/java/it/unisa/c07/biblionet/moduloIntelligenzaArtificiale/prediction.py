import pickle
import pandas as pd
import flask
from flask import jsonify, request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Funzione per leggere il modello dal file
def readModel():
    read_file = open('model.obj', 'rb')
    model = pickle.load(read_file)
    return model

@app.route('/predict', methods=['POST'])
def makePrediction(ans1, ans2, ans3, ans4, ans5):
    model = readModel()

    answers = {ans1, ans2, ans3, ans4, ans5}

    predictions = []
    probabilities = []

    i = 0

    for answer in answers:
        predictions.append(
            model.predict(pd.DataFrame({'answer': [answer]}))
        )
        prediction_frame = pd.DataFrame(predictions[i])
        data_frame = pd.DataFrame({'char1': [prediction_frame.loc[0, 'char1']],
                                   'char2': [prediction_frame.loc[0, 'char2']],
                                   'char3': [prediction_frame.loc[0, 'char3']],
                                   'answer': [answer]})
        probabilities.append(
            model.predict_probability(data_frame)
        )
        i += 1

    results = []
    for j in range(0, 5):
        tmp = pd.DataFrame(predictions[j])
        results.append(tmp.loc[0, 'genre'])

    print(results)
    return results


@app.route('/', methods=['POST'])
def home():

    json = request.json
    print(json['ans1'])

    return jsonify(makePrediction(json['ans1'], json['ans2'], json['ans3'], json['ans4'], json['ans5']))

app.run()
