import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import BayesianEstimator
from pgmpy.estimators import MaximumLikelihoodEstimator
from random import randint
from pgmpy.estimators import ParameterEstimator
import math

#CREO UNA LISTA DI INTERI CHE USERO' PER DIRE AL METODO
#READ_EXCEL QUALI COLONNE DEVE PRENDERE (PER PRENDERE SOLO 4 DOMANDE)
#FACCIO CICLO FINCHE' NON HO SCELTO 4 COLONNE, TUTTE DIVERSE
questions_list = []
while len(questions_list) < 4:
    value = randint(0, 24)
    if not questions_list.__contains__(value):
        questions_list.append(value)

#INSERISCO MANUALMENTE NELL'ARRAY LE ULTIME 4 COLONNE CHE
#CONTENGONO CARATTERISTICHE E GENERE
questions_list.append(25)
questions_list.append(26)
questions_list.append(27)
questions_list.append(28)

#LEGGO DALL'EXCEL USANDO SOLO LE COLONNE I CUI INDICI SONO IN QUELL'ARRAY
excel = pd.read_excel(r'dataset/dataset.xlsx', usecols=questions_list)

#CREO UN DATAFRAME CHIAMATO DATASET IN CUI METTO I VALORI PRESI
#DALLE RIGHE DELL'EXCEL LETTO E IMPOSTO LE COLONNE COI NOMI CHE
#MI SERVONO PER FARLI MATCHARE CON I PARAMETRI CHE USERA' IL MODELLO BAYESIANO
#DOPO FACCIO DROPNA PER SICUREZZA (NEL CASO SI PRENDA RIGHE NA DALL'EXCEL)
dataset = pd.DataFrame(excel.values, columns=['user_answer', 'user_answer1', 'user_answer2',
                                       'user_answer3', 'car_genre', 'car_genre1',
                                       'car_genre2', 'genre'])
dataset = dataset.dropna()

#CREO LA RETE BAEYESIANA. ANSWERS -> CARATTERISTICHE -> GENERE
model = BayesianModel([('user_answer', 'car_genre'), ('user_answer', 'car_genre1'), ('user_answer', 'car_genre2'),
                       ('user_answer1', 'car_genre'), ('user_answer1', 'car_genre1'), ('user_answer1', 'car_genre2'),
                       ('user_answer2', 'car_genre'), ('user_answer2', 'car_genre1'), ('user_answer2', 'car_genre2'),
                       ('user_answer3', 'car_genre'), ('user_answer3', 'car_genre1'), ('user_answer3', 'car_genre2'),
                       ('car_genre', 'genre'), ('car_genre1', 'genre'), ('car_genre2', 'genre')])


#CALCOLO IL 90% DELLE RIGHE DEL DATASET E LE USO PER TRAINARE
#IL RESTANTE 10% VERRA' USATO PER PROVATE A FARE PREDICT
#DATASET[:X] SIGNIFICA PRENDI TUTTE LE RIGHE FINO ALLA RIGA X
#DATASET[X:] SIGNIFICA PRENDI TUTTE LE RIGHE DA X IN POI
train_number = int(math.ceil((len(dataset) / 100) * 90))-1
train_data = dataset[:train_number]
predict_data = dataset[train_number:]


#FACCIO FITTING (TRAINING) DEL MODELLO E USO UN BAYESIAN ESTIMATOR
#DA DEI WARNING IGNORA
model.fit(train_data, BayesianEstimator)
print("Proprietà Rete Baeysiana rispettate:", model.check_model())


#TOLGO LE COLONNE CON GENERE E CARATTERISTICHE
#DAL DATASET DI TEST PER FARE IN MODO CHE LI PREDICTI
#SOLO SULLA BASE DELLE RISPOSTE
predict_data.pop('genre')
predict_data.pop('car_genre')
predict_data.pop('car_genre1')
predict_data.pop('car_genre2')
print(predict_data['user_answer'])
print(predict_data['user_answer1'])
print(predict_data['user_answer2'])
print(predict_data['user_answer3'])

predicted = model.predict(predict_data)
print(predicted)



#PROVO A PREDICTARE UN GENERE DATE LE CARATTERISTICHE
#PRENDO L'ULTIMA RIGA DEL DATASET E CI LEVO GENERE E RISPOSTE
#POI STAMPO IL GENERE PREDICTATO (LUI PREDICTA TUTTI I NODI DELLA RETE
#CHE NON TROVA NEI DATI IN INPUT AL PREDICT, QUINDI IN QUESTO CASO
#HA PREDICTATO ANCHE LE RISPOSTE
to_predict = dataset[123:]
to_predict.pop('user_answer')
to_predict.pop('user_answer1')
to_predict.pop('user_answer2')
to_predict.pop('user_answer3')
to_predict.pop('genre')
print(to_predict)

predicted = model.predict(to_predict)

print(predicted['genre'])
