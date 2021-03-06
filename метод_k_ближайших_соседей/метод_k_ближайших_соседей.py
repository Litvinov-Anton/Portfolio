# -*- coding: utf-8 -*-
"""Метод k -ближайших соседей.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GwkIhUygrfMGw_a2d0IV7jsLISD1dLLq

**Метод  k -ближайших соседей**
"""

#Чтение данных

import pandas as pd
train_data = pd.read_csv("/content/Task_data.csv", delimiter=',', index_col='id')

#Вывод всех строк данных

print(train_data)

#Отбор данных для предикторов, удаление столбца Class

X = pd.DataFrame(train_data.drop(['Class'], axis=1))

#Отбор столбца Class для отклика

y = pd.DataFrame(train_data['Class']).values.ravel()

#Подключение библиотеки и задание параметров модели: n_neighbors — число соседей; p — используемое расстояние. Манхэттенское расстояние — p=1, евклидово расстояние — p=2. Дополнительные параметры — https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html

from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=3, p=2)
neigh.fit(X, y)
KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
           metric_params=None, n_jobs=None, n_neighbors=3, p=2,
           weights='uniform')

#Новый объект, который необходимо классифицировать

NewObject = [5, -4]

#Назначенный класс:

neigh.predict([NewObject])
#array([1])
#Вероятности отнесения к классам 0 и 1 соответственно:

neigh.predict_proba([NewObject])
#array([[0.33333333, 0.66666667]])
#Вывод расстояний до  k  соседей в порядке удаления (первый массив — расстояния, второй — идентификаторы объектов). Обращаем внимание, что метод возвращает индексы ближайших соседей с нуля, что не соответствует индексации в таблице.

neigh.kneighbors([NewObject])
#(array([[26.92582404, 34.0147027 , 48.27007354]]), array([[0, 5, 3]]))
#Получены индексы [0, 5, 3], значит id = [1, 6, 4]