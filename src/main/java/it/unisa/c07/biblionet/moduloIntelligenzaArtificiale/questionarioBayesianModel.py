import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import BayesianEstimator
import math
import networkx as nx
import pickle


# Funzione per salvare e aggiornare il modello in un file
def saveModel(model):
    save_file = open("model.obj", 'wb')
    pickle.dump(model, save_file)


# Leggo dall'excel il dataset
excel = pd.read_excel(r'dataset/dataset.xlsx')

# Creo un DataFrame con una risposta, tre caratteristiche e un genere
i = 0
dataset = pd.DataFrame(columns=['answer', 'char1', 'char2', 'char3', 'genre'])

# Costruisco dall'excel il dataframe, salvandomi per ogni riga una risposta, le caratteristiche e il genere
for row in excel.values:
    for column in range(25):
        dataset.loc[i, 'answer'] = row[column]
        dataset.loc[i, 'char1'] = row[25]
        dataset.loc[i, 'char2'] = row[26]
        dataset.loc[i, 'char3'] = row[27]
        dataset.loc[i, 'genre'] = row[28]
        i += 1

# Costruisco la rete bayesiana ANSWER -> CHARACTERISTICS -> GENRE
model = BayesianModel([('answer', 'char1'), ('answer', 'char2'), ('answer', 'char3'),
                       ('char1', 'genre'), ('char2', 'genre'), ('char3', 'genre')])
nx.draw(model, with_labels=True)

# Prelevo il 70% dei dati per il training e il 10% è lasciato per il testing
dataset = dataset.sample(frac=1)
train_number = int(math.ceil((len(dataset) / 100) * 70)) - 1
train_data = dataset[:train_number]
predict_data = dataset[train_number:]

# Effettuo il fitting dei dati di training usando un Bayesian Estimator
model.fit(train_data, BayesianEstimator)
print("Proprietà Rete Baeysiana rispettate:", model.check_model())

saveModel(model)

test_value = predict_data.pop('genre')
predict_data.pop('char1')
predict_data.pop('char2')
predict_data.pop('char3')

prediction = model.predict(predict_data)
prediction = prediction['genre']

count = 0

for i in range(len(test_value)):
    if prediction.values[i] == test_value.values[i]:
        count += 1

percent = count * 100 / len(test_value)
formatted_percent = "{:.2f}".format(percent)

print(str("Accuracy: " + formatted_percent) + "%")
