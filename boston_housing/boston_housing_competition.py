"""
File: boston_housing_competition.py
Name: Tony
--------------------------------
This file demonstrates how to analyze boston
housing dataset. Students will upload their 
results to kaggle.com and compete with people
in class!

You are allowed to use pandas, sklearn, or build the
model from scratch! Go data scientists!
"""
import os
import glob
import pandas as pd
from sklearn import linear_model, metrics, model_selection, preprocessing
import numpy as np
import matplotlib.pyplot as plt

folder_path = 'boston'
out_path = "boston_weight"
file = "boston_2.9*.csv" or "boston_2.8*.csv"
count = 6


def main():
	global folder_path, out_path, file, count
	w2 = 0.3
	w3 = 0.45
	w1 = 1 - w2 - w3
	sum = 0
	# for i in range(100):
	# 	train_data = pd.read_csv('boston_housing/train.csv')
	# 	test_data = pd.read_csv('boston_housing/test.csv')
	# 	train_data, val_data = model_selection.train_test_split(train_data, test_size=0.2)
	# 	feature = ['crim', 'zn', 'nox', 'rm', 'indus', 'age', 'rad', 'tax', 'ptratio', 'black', 'lstat']
	# 	y = train_data.medv
	# 	y1 = val_data.medv
	# 	x_train = train_data[feature]
	# 	xv_train = val_data[feature]
	# 	extractor = preprocessing.PolynomialFeatures(degree=2)
	# 	x_2 = extractor.fit_transform(x_train)
	# 	xv_2 = extractor.fit_transform(xv_train)
	# 	h1 = linear_model.ElasticNet(alpha=0.01)
	# 	h1.fit(x_2, y)
	# 	c1 = h1.predict(x_2)
	# 	cv1 = h1.predict(xv_2)
	# 	h2 = linear_model.Lasso(alpha=50)
	# 	h2.fit(x_2, y)
	# 	c2 = h2.predict(x_2)
	# 	cv2 = h2.predict(xv_2)
	# 	h3 = linear_model.Ridge(alpha=50)
	# 	h3.fit(x_2, y)
	# 	c3 = h3.predict(x_2)
	# 	cv3 = h3.predict(xv_2)
	# 	c = c1*w1+c2*w2+c3*w3
	# 	c1 = cv1*w1+cv2*w2+cv3*w3
	# 	e = round((metrics.mean_squared_error(y1, c1) ** 0.5), 5)
	# 	sum += e
	# 	print(metrics.mean_squared_error(y1, c1) ** 0.5)
	#
	# 	# Test_data
	# 	id = test_data.ID.tolist()
	# 	x_test = test_data[feature]
	# 	test = extractor.transform(x_test)
	# 	v1 = h1.predict(test)
	# 	v2 = h2.predict(test)
	# 	v3 = h3.predict(test)
	# 	v = v1*w1 + v2*w2 + v3*w3
	# 	if e <= 3.2:
	# 		out_file(v, 'boston/boston_'+str(e)+'.csv', ID=id)
	file_paths = glob.glob(os.path.join(folder_path, file))
	combined_data = pd.DataFrame()
	for file in file_paths:
		df = pd.read_csv(file)
		combined_data = pd.concat([combined_data, df])
	average = combined_data.groupby('ID').mean()
	print(average)
	count += 1
	output_file = "boston_weight_average_"+str(count)+'.csv'
	average.to_csv(os.path.join(out_path, output_file), index=True)


def out_file(predictions, filename, ID):
	"""
	: param predictions: numpy.array, a list-like data structure that stores 0's and 1's
	: param filename: str, the filename you would like to write the results to
	"""
	print('\n===============================================')
	print(f'Writing predictions to --> {filename}')
	with open(filename, 'w', encoding='utf-8') as out:
		out.write('ID,medv\n')
		start_id = ID
		i = 0
		for ans in predictions:
			out.write(str(start_id[i])+','+str(ans)+'\n')
			i += 1
	print('===============================================')


if __name__ == '__main__':
	main()
