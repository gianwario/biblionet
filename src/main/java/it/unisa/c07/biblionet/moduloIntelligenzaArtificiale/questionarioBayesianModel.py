import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import BayesianEstimator
from pgmpy.estimators import MaximumLikelihoodEstimator
from random import randint
from pgmpy.estimators import ParameterEstimator
import math
import networkx as nx
import matplotlib.pyplot as plt
from pgmpy.inference import VariableElimination


#Leggo dall'excel il dataset
excel = pd.read_excel(r'dataset/dataset.xlsx')

#Creo un DataFrame con una risposta, tre caratteristiche e un genere
i = 0
dataset = pd.DataFrame(columns=['answer', 'char1', 'char2', 'char3', 'genre'])

#Costruisco dall'excel il dataframe, salvandomi per ogni riga una risposta, le caratteristiche e il genere
for row in excel.values:
    for column in range(25):
        dataset.loc[i, 'answer'] = row[column]
        dataset.loc[i, 'char1'] = row[25]
        dataset.loc[i, 'char2'] = row[26]
        dataset.loc[i, 'char3'] = row[27]
        dataset.loc[i, 'genre'] = row[28]
        i += 1

print(dataset[:50])

#Costruisco la rete bayesiana ANSWER -> CHARACTERISTICS -> GENRE
model = BayesianModel([('answer', 'char1'), ('answer', 'char2'), ('answer', 'char3'),
                       ('char1', 'genre'), ('char2', 'genre'), ('char3', 'genre')])
nx.draw(model, with_labels = True)

#Prelevo il 90% dei dati per il training e il 10% è lasciato per il testing
train_number = int(math.ceil((len(dataset) / 100) * 90))-1
train_data = dataset[:train_number]
predict_data = dataset[train_number:]

#Effettuo il fitting dei dati di training usando un Bayesian Estimator
model.fit(train_data, BayesianEstimator)
print("Proprietà Rete Baeysiana rispettate:", model.check_model())


test = model.predict(pd.DataFrame({'answer' : ["Amaro"]}))
print(test)

test_value = predict_data.pop('genre')
predict_data.pop('char1')
predict_data.pop('char2')
predict_data.pop('char3')

prediction = model.predict(predict_data)
prediction = prediction['genre']

count = 0

print(len(prediction))
print(len(test_value))

for i in range(len(test_value)):
    if prediction.values[i] == test_value.values[i]:
        count+=1

print(count)
print(str(len(test_value)))

percent = count * 100 / len(test_value)

print(str(percent) + "%")


