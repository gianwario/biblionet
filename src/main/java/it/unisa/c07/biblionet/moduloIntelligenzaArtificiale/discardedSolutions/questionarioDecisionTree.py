import pandas as pd
from random import randint
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

questions_list = []
while len(questions_list) < 4:
    value = randint(0, 7)
    if not questions_list.__contains__(value):
        questions_list.append(value)


questions_list.append(29)
print(questions_list)

excel = pd.read_excel(r'dataset/dataset.xlsx', usecols=questions_list)

dataset = pd.DataFrame(excel.values, columns=['user_answer', 'user_answer1', 'user_answer2',
                                       'user_answer3', 'genre'])
dataset = dataset.dropna()
print(dataset)

cols = ['user_answer', 'user_answer1', 'user_answer2', 'user_answer3']
x = dataset[cols]
y = dataset['genre']
x = pd.get_dummies(x)
y = pd.get_dummies(y)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1) # 70% training and 30% test

print(x_train)
print(y_train)
print(x_test)
print(y_test)

clf = RandomForestClassifier(max_depth=2, random_state=0)
clf = clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))