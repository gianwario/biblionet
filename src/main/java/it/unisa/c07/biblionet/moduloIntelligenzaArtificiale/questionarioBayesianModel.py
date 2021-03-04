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

# Leggo i dati dal file excel
excel = pd.read_excel(r'dataset/dataset.xlsx')

# Creo un DataFrame con una risposta, tre caratteristiche e un genere
i = 0
dataset = pd.DataFrame(columns=['answer', 'char1', 'char2', 'char3', 'genre'])

# Costruisco dall'excel il dataframe, salvandomi per ogni riga una risposta, le caratteristiche e il genere.
# In questo modo, per ogni persona che ha partecipato alla creazione del dataset, considero per ogni risposta data
# una diretta associazione al genere e quindi alle caratteristiche
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

# Prelevo il 70% dei dati per il training e il 30% è lasciato per il testing, in modo da calcolare
# una percentuale di accuracy. Inoltre, randomizzo le righe del dataset
dataset = dataset.sample(frac=1)
train_number = int(math.ceil((len(dataset) / 100) * 70)) - 1
train_data = dataset[:train_number]
predict_data = dataset[train_number:]

# Effettuo il fitting dei dati di training usando un Bayesian Estimator
model.fit(train_data, BayesianEstimator, prior_type='BDeu', equivalent_sample_size=5)
print("Proprietà Rete Baeysiana rispettate:", model.check_model())

# Memorizzo il modello già allenato (ovvero con le CPD calcolate)
# in modo che lo possa leggere nel file per le prediction
saveModel(model)

# Creo un lista contenente solo i Generi dai predict_data
# in seguito rimuovo le caratteristiche.
# In questo modo, test_value contiene una lista di generi
# e predict_data contiene una lista di user answer
test_value = predict_data.pop('genre')
predict_data.pop('char1')
predict_data.pop('char2')
predict_data.pop('char3')

# Effettuo la predizione dei dati grazie al modello bayesiano allenato
# in precedenza, e memorizzo solo le informazioni relative al genere restituito
prediction = model.predict(predict_data)
prediction = prediction['genre']

# Controllo, per ogni valore predictato, se è uguale alla label che ho
# precedentemente rimosso, quindi se il genere predetto coincide con quello
# del campione in esame
count = 0
for i in range(len(test_value)):
    if prediction.values[i] == test_value.values[i]:
        count += 1

# Calcolo la percentuale di risposte corrette sulla base
# del numero di campioni testati e la stampo in percentuale
percent = count * 100 / len(test_value)
formatted_percent = "{:.2f}".format(percent)
print(str("Accuracy: " + formatted_percent) + "%")
