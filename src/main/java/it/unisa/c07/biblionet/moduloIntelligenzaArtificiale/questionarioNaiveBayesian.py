import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import BayesianEstimator
from pgmpy.estimators import MaximumLikelihoodEstimator
from random import randint
from pgmpy.estimators import ParameterEstimator
import math

questions_list = []
while len(questions_list) < 4:
    value = randint(0, 7)
    if not questions_list.__contains__(value):
        questions_list.append(value)


questions_list.append(8)
questions_list.append(9)
questions_list.append(10)
questions_list.append(11)

excel = pd.read_excel(r'dataset/dataset.xlsx', usecols=questions_list)

dataset = pd.DataFrame(excel.values, columns=['user_answer', 'user_answer1', 'user_answer2',
                                       'user_answer3', 'car_genre', 'car_genre1',
                                       'car_genre2', 'genre'])
dataset = dataset.dropna()

model = BayesianModel([('user_answer', 'car_genre'), ('user_answer', 'car_genre1'), ('user_answer', 'car_genre2'),
                       ('user_answer1', 'car_genre'), ('user_answer1', 'car_genre1'), ('user_answer1', 'car_genre2'),
                       ('user_answer2', 'car_genre'), ('user_answer2', 'car_genre1'), ('user_answer2', 'car_genre2'),
                       ('user_answer3', 'car_genre'), ('user_answer3', 'car_genre1'), ('user_answer3', 'car_genre2'),
                       ('car_genre', 'genre'), ('car_genre1', 'genre'), ('car_genre2', 'genre')])


train_number = int(math.ceil((len(dataset) / 100) * 70))-1

train_data = dataset[:train_number]
predict_data = dataset[train_number:]

predict_data.pop('genre')
predict_data.pop('car_genre')
predict_data.pop('car_genre1')
predict_data.pop('car_genre2')

model.fit(train_data, MaximumLikelihoodEstimator)

# est = BayesianEstimator(model, dataset)
# print(est.estimate_cpd('genre', prior_type='BDeu', equivalent_sample_size=10))

print("Proprietà Rete Baeysiana rispettate:", model.check_model())

predicted = model.predict(predict_data)
print(predict_data['user_answer'])
print(predict_data['user_answer1'])
print(predict_data['user_answer2'])
print(predict_data['user_answer3'])
print(predicted)
