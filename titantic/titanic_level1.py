"""
File: titanic_level1.py
Name: Tony
----------------------------------
This file builds a machine learning algorithm from scratch 
by Python. We'll be using 'with open' to read in dataset,
store data into a Python dict, and finally train the model and 
test it on kaggle website. This model is the most flexible among all
levels. You should do hyper-parameter tuning to find the best model.
"""

import math
from util import dotProduct, increment
TRAIN_FILE = 'titanic_data/train.csv'
TEST_FILE = 'titanic_data/test.csv'
avg_age = 0
avg_fare = 0


def data_preprocess(filename: str, data: dict, mode='Train', training_data=None):
	"""
	:param filename: str, the filename to be processed
	:param data: an empty Python dictionary
	:param mode: str, indicating if it is training mode or testing mode
	:param training_data: dict[str: list], key is the column name, value is its data
						  (You will only use this when mode == 'Test')
	:return data: dict[str: list], key is the column name, value is its data
	"""
	global avg_age, avg_fare
	is_head = True
	sum_age = 0
	sum_fare = 0
	with open(filename, 'r') as f:
		data = {}
		for line in f:
			data_list = line.strip().split(",")
			if is_head:
				is_head = False
				title = data_list
				if mode == 'Train':
					for i in range(len(title)):
						if i == 1 or i == 2 or i == 4 or i == 5 or i == 6 or i == 7 or i == 9 or i == 11:
							data[title[i]] = []
				else:
					for i in range(len(title)):
						if i == 1 or i == 3 or i == 4 or i == 5 or i == 6 or i == 8 or i == 10:
							data[title[i]] = []
			else:
				if mode == 'Train' and (data_list[6] == "" or data_list[12] == ""):
					pass
				else:
					for i in range(len(data_list)):
						if i == 1 and mode == 'Train':
							data['Survived'].append(int(data_list[i]))
						if (i == 2 and mode == 'Train') or (mode == 'Test' and i == 1):
							data['Pclass'].append(int(data_list[i]))
						if (i == 5 and mode == 'Train') or (mode == 'Test' and i == 4):
							if data_list[i] == "male":
								data['Sex'].append(1)
							else:
								data['Sex'].append(0)
						if (i == 6 and mode == 'Train') or (mode == 'Test' and i == 5):
							if data_list[i] != "":
								data['Age'].append(float(data_list[i]))
							else:
								data['Age'].append(float(avg_age))
							if mode == 'Train':
								sum_age += float(data_list[i])
								avg_age = round(sum_age / len(data['Age']), 3)
						if (i == 7 and mode == 'Train') or (mode == 'Test' and i == 6):
							data['SibSp'].append(int(data_list[i]))
						if (i == 8 and mode == 'Train') or (mode == 'Test' and i == 7):
							data['Parch'].append(int(data_list[i]))
						if (i == 10 and mode == 'Train') or (mode == 'Test' and i == 9):
							if data_list[i] != "":
								data['Fare'].append(float(data_list[i]))
							else:
								data['Fare'].append(float(avg_fare))
							if mode == 'Train':
								sum_fare += float(data_list[i])
								avg_fare = round(sum_fare / len(data['Fare']), 3)
						if (i == 12 and mode == 'Train') or (mode == 'Test' and i == 11):
							if data_list[i] == "S":
								data['Embarked'].append(0)
							elif data_list[i] == "C":
								data['Embarked'].append(1)
							else:
								data['Embarked'].append(2)
	return data


def one_hot_encoding(data: dict, feature: str):
	"""
	:param data: dict[str, list], key is the column name, value is its data
	:param feature: str, the column name of interest
	:return data: dict[str, list], remove the feature column and add its one-hot encoding features
	"""
	if feature == 'Sex':
		data['Sex_0'] = []
		data['Sex_1'] = []
		for i in range(len(data['Sex'])):
			if data['Sex'][i] == 1:
				data['Sex_0'].append(0)
				data['Sex_1'].append(1)
			else:
				data['Sex_0'].append(1)
				data['Sex_1'].append(0)
		del data['Sex']
	if feature == 'Pclass':
		data['Pclass_0'] = []
		data['Pclass_1'] = []
		data['Pclass_2'] = []
		for i in range(len(data['Pclass'])):
			if data['Pclass'][i] == 1:
				data['Pclass_0'].append(1)
				data['Pclass_1'].append(0)
				data['Pclass_2'].append(0)
			elif data['Pclass'][i] == 2:
				data['Pclass_0'].append(0)
				data['Pclass_1'].append(1)
				data['Pclass_2'].append(0)
			else:
				data['Pclass_0'].append(0)
				data['Pclass_1'].append(0)
				data['Pclass_2'].append(1)
		del data['Pclass']
	if feature == 'Embarked':
		data['Embarked_0'] = []
		data['Embarked_1'] = []
		data['Embarked_2'] = []
		for i in range(len(data['Embarked'])):
			if data['Embarked'][i] == 0:
				data['Embarked_0'].append(1)
				data['Embarked_1'].append(0)
				data['Embarked_2'].append(0)
			elif data['Embarked'][i] == 1:
				data['Embarked_0'].append(0)
				data['Embarked_1'].append(1)
				data['Embarked_2'].append(0)
			else:
				data['Embarked_0'].append(0)
				data['Embarked_1'].append(0)
				data['Embarked_2'].append(1)
		del data['Embarked']
	return data


def normalize(data: dict):
	"""
	:param data: dict[str, list], key is the column name, value is its data
	:return data: dict[str, list], key is the column name, value is its normalized data
	"""
	min_age, max_age = min(data['Age']), max(data['Age'])
	min_sibsp, max_sibsp = min(data['SibSp']), max(data['SibSp'])
	min_parch, max_parch = min(data['Parch']), max(data['Parch'])
	min_fare, max_fare = min(data['Fare']), max(data['Fare'])
	for i in range(len(data['Age'])):
		data['Age'][i] = (data['Age'][i]-min_age)/(max_age-min_age)
	for i in range(len(data['SibSp'])):
		data['SibSp'][i] = (data['SibSp'][i] - min_sibsp) / (max_sibsp-min_sibsp)
	for i in range(len(data['Parch'])):
		data['Parch'][i] = (data['Parch'][i] - min_parch) / (max_parch-min_parch)
	for i in range(len(data['Fare'])):
		data['Fare'][i] = (data['Fare'][i] - min_fare) / (max_fare-min_fare)
	return data


def learnPredictor(inputs: dict, labels: list, degree: int, num_epochs: int, alpha: float):
	"""
	:param inputs: dict[str, list], key is the column name, value is its data
	:param labels: list[int], indicating the true label for each data
	:param degree: int, degree of polynomial features
	:param num_epochs: int, the number of epochs for training
	:param alpha: float, known as step size or learning rate
	:return weights: dict[str, float], feature name and its weight
	"""
	# Step 1 : Initialize weights
	weights = {}  # feature => weight
	keys = list(inputs.keys())
	if degree == 1:
		for i in range(len(keys)):
			weights[keys[i]] = 0
	elif degree == 2:
		for i in range(len(keys)):
			weights[keys[i]] = 0
		for i in range(len(keys)):
			for j in range(i, len(keys)):
				weights[keys[i] + keys[j]] = 0
	# Step 2 : Start training
	if degree == 1:
		for epoch in range(num_epochs):
			for i in range(len(inputs[keys[0]])):
				feature = {}
				for j in range(len(keys)):
					feature[keys[j]] = inputs[keys[j]][i]
				y = labels[i]
				h = 1 / (1 + math.exp(-dotProduct(feature, weights)))
				scale = -(alpha * (h - y))
				increment(weights, scale, feature)
	elif degree == 2:
		for epoch in range(num_epochs):
			for i in range(len(inputs[keys[0]])):
				feature = {}
				for j in range(len(keys)):
					feature[keys[j]] = inputs[keys[j]][i]
				for j in range(len(keys)):
					for k in range(j, len(keys)):
						feature[keys[j] + keys[k]] = inputs[keys[j]][i]*inputs[keys[k]][i]
				y = labels[i]
				h = 1 / (1 + math.exp(-dotProduct(feature, weights)))
				scale = -(alpha * (h - y))
				increment(weights, scale, feature)
	return weights
