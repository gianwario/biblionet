import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator
from random import randint
import math

questions_list = []
while len(questions_list) < 5:
    value = randint(0, 7)
    if not questions_list.__contains__(value):
        questions_list.append(value)


questions_list.append(8)
questions_list.append(9)
questions_list.append(10)
questions_list.append(11)
print(questions_list)

excel = pd.read_excel(r'dataset/dataset.xlsx', usecols=questions_list)
dataset = pd.DataFrame(excel)
dataset = dataset.dropna()


dataset.columns.values[0] = "user_answer"
dataset.columns.values[1] = "user_answer1"
dataset.columns.values[2] = "user_answer2"
dataset.columns.values[3] = "user_answer3"
dataset.columns.values[4] = "user_answer4"
dataset.columns.values[5] = "car_genre"
dataset.columns.values[6] = "car_genre1"
dataset.columns.values[7] = "car_genre2"
dataset.columns.values[8] = "genre"

print(dataset)

model = BayesianModel([('user_answer', 'car_genre'), ('user_answer', 'car_genre1'), ('user_answer', 'car_genre2'),
                       ('user_answer1', 'car_genre'), ('user_answer1', 'car_genre1'), ('user_answer1', 'car_genre2'),
                       ('user_answer2', 'car_genre'), ('user_answer2', 'car_genre1'), ('user_answer2', 'car_genre2'),
                       ('user_answer3', 'car_genre'), ('user_answer3', 'car_genre1'), ('user_answer3', 'car_genre2'),
                       ('user_answer4', 'car_genre'), ('user_answer4', 'car_genre1'), ('user_answer4', 'car_genre2'),
                       ('car_genre', 'genre'), ('car_genre1', 'genre'), ('car_genre2', 'genre')])


train_number = int(math.ceil((len(dataset) / 100) * 70))-1

train_data = dataset[:train_number]
predict_data = dataset[train_number:]

print(train_number)

predict_data.pop('car_genre')
predict_data.pop('car_genre1')
predict_data.pop('car_genre2')
predict_data.pop('genre')

model.fit(train_data, MaximumLikelihoodEstimator)
print("Proprietà Rete Baeysiana rispettate:", model.check_model())

predicted = pd.DataFrame(model.predict(predict_data))
print(predicted)




