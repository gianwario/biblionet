import pickle
import pandas as pd
import sys

print("a")
#Funzione per leggere il modello dal file
def readModel():
    read_file = open('model.obj', 'rb')
    model = pickle.load(read_file)
    return model

model = readModel()

answers = {sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]}
# answ1 = "Amaro"
# answ2 = "Riflessivo, logico, osservatore"
# answ3 = "Cinema, teatro, SerieTV"
# answ4 = "Non li guardo perché non mi interessa il genere"
# answ5 = "Acqua"
# answers = [answ1, answ2, answ3, answ4, answ5]
predictions = []
probabilities = []

i = 0

for answer in answers:
    predictions.append(
        model.predict(pd.DataFrame({'answer' : [answer]}))
    )
    prediction_frame = pd.DataFrame(predictions[i])
    data_frame = pd.DataFrame({'char1' : [prediction_frame.loc[0, 'char1']],
                               'char2' : [prediction_frame.loc[0, 'char2']],
                               'char3' : [prediction_frame.loc[0, 'char3']],
                               'answer' : [answer]})
    probabilities.append(
        model.predict_probability(data_frame)
    )
    i += 1

results = pd.DataFrame(predictions[0])
print(results.loc[0, 'genre'])

def predict(arg1,arg2,arg3,arg4,arg5):
    return "cazzomreda"




