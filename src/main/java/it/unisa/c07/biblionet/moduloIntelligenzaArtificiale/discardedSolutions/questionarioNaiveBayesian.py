import classeval
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
from random import randint
import math
import df2onehot

#LEGGO DALL'EXCEL USANDO SOLO LE COLONNE I CUI INDICI SONO IN QUELL'ARRAY
excel = pd.read_excel(r'dataset/formatted_dataset.xlsx', usecols=[0,1,2,3,4,8])
ds = pd.DataFrame(columns=['user_answer', 'user_answer1', 'user_answer2',
                                       'user_answer3', 'user_answer4', 'genre'])


#CREO UN DATAFRAME CHIAMATO DATASET IN CUI METTO I VALORI PRESI
#DALLE RIGHE DELL'EXCEL LETTO E IMPOSTO LE COLONNE COI NOMI CHE
#MI SERVONO PER FARLI MATCHARE CON I PARAMETRI CHE USERA' IL MODELLO BAYESIANO
#DOPO FACCIO DROPNA PER SICUREZZA (NEL CASO SI PRENDA RIGHE NA DALL'EXCEL)
dataset = pd.DataFrame(excel.values, columns=['user_answer', 'user_answer1', 'user_answer2',
                                       'user_answer3', 'user_answer4', 'genre'])
dataset = dataset.dropna()



X = dataset
y = X.pop('genre')
print(X)
print(y)
X = pd.get_dummies(X)
X_train, X_test, y_train, y_test = train_test_split(X, y)

model = MultinomialNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Number of mislabeled points out of a total %d points : %d"
      % (X_test.shape[0], (y_test != y_pred).sum()))
