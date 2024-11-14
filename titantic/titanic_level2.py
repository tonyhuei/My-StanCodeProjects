"""
File: titanic_level2.py
Name: 
----------------------------------
This file builds a machine learning algorithm by pandas and sklearn libraries.
We'll be using pandas to read in dataset, store data into a DataFrame,
standardize the data by sklearn, and finally train the model and
test it on kaggle website. Hyper-parameters tuning are not required due to its
high level of abstraction, which makes it easier to use but less flexible.
You should find a good model that surpasses 77% test accuracy on kaggle.
"""

import math
import pandas as pd
from sklearn import preprocessing, linear_model
nan_cache = {}

TRAIN_FILE = 'titanic_data/train.csv'
TEST_FILE = 'titanic_data/test.csv'


def data_preprocess(filename, mode='Train', training_data=None):
	"""
	:param filename: str, the filename to be read into pandas
	:param mode: str, indicating the mode we are using (either Train or Test)
	:param training_data: DataFrame, a 2D data structure that looks like an excel worksheet
						  (You will only use this when mode == 'Test')
	:return: Tuple(data, labels), if the mode is 'Train'; or return data, if the mode is 'Test'
	"""
	data = pd.read_csv(filename)
	labels = None
	pop_c = ['PassengerId', 'Name', 'Ticket', 'Cabin']
	data['Embarked'].replace(['S', 'C', 'Q'], [0, 1, 2], inplace=True)
	data['Sex'].replace(['female', 'male'], [0, 1], inplace=True)
	for i in range(len(pop_c)):
		data.pop(pop_c[i])
	if mode == 'Train':
		data.dropna(axis=0, subset=['Age', 'Embarked'], inplace=True)
		labels = data.pop('Survived')
		nan_cache['Age'] = round(data.Age.mean(), 3)
		nan_cache['Fare'] = round(data.Fare.mean(), 3)
		return data, labels
	elif mode == 'Test':
		data.Age.fillna(nan_cache['Age'], inplace=True)
		data.Fare.fillna(nan_cache['Fare'], inplace=True)
		return data


def one_hot_encoding(data, feature):
	"""
	:param data: DataFrame, key is the column name, value is its data
	:param feature: str, the column name of interest
	:return data: DataFrame, remove the feature column and add its one-hot encoding features
	"""
	if feature == 'Sex':
		data['Sex_1'] = 0
		data.loc[data.Sex == 1, 'Sex_1'] = 1
		data['Sex_0'] = 0
		data.loc[data.Sex == 0, 'Sex_0'] = 1
		data.pop('Sex')
	if feature == 'Pclass':
		data['Pclass_0'] = 0
		data.loc[data.Pclass == 1, 'Pclass_0'] = 1
		data['Pclass_1'] = 0
		data.loc[data.Pclass == 2, 'Pclass_1'] = 1
		data['Pclass_2'] = 0
		data.loc[data.Pclass == 3, 'Pclass_2'] = 1
		data.pop('Pclass')
	if feature == 'Embarked':
		data['Embarked_0'] = 0
		data.loc[data.Embarked == 0, 'Embarked_0'] = 1
		data['Embarked_1'] = 0
		data.loc[data.Embarked == 1, 'Embarked_1'] = 1
		data['Embarked_2'] = 0
		data.loc[data.Embarked == 2, 'Embarked_2'] = 1
		data.pop('Embarked')
	return data


def standardization(data, mode='Train'):
	"""
	:param data: DataFrame, key is the column name, value is its data
	:param mode: str, indicating the mode we are using (either Train or Test)
	:return data: DataFrame, standardized features
	"""
	if mode == 'Train':
		standardize = preprocessing.StandardScaler()
		data = standardize.fit_transform(data)
	return data


def main():
	"""
	You should call data_preprocess(), one_hot_encoding(), and
	standardization() on your training data. You should see ~80% accuracy on degree1;
	~83% on degree2; ~87% on degree3.
	Please write down the accuracy for degree1, 2, and 3 respectively below
	(rounding accuracies to 8 decimal places)
	TODO: real accuracy on degree1 -> 0.80196629
	TODO: real accuracy on degree2 -> 0.83707865
	TODO: real accuracy on degree3 -> 0.87640449
	"""
	train_data = data_preprocess(TRAIN_FILE, mode='Train')
	y = train_data[1]
	train_data = train_data[0]
	one_hot_encoding(train_data, feature='Sex')
	one_hot_encoding(train_data, feature='Pclass')
	one_hot_encoding(train_data, feature='Embarked')
	standardize = preprocessing.StandardScaler()
	train_data = standardize.fit_transform(train_data)
	for i in range(3):
		h = linear_model.LogisticRegression(max_iter=10000)
		poly_phi_extractor = preprocessing.PolynomialFeatures(degree=i+1)
		train_data_poly = poly_phi_extractor.fit_transform(train_data)
		classifier = h.fit(train_data_poly, y)
		print('Degree', str((i+1)), 'Training Acc:', classifier.score(train_data_poly, y))


if __name__ == '__main__':
	main()
