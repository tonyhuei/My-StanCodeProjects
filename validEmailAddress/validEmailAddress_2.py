"""
File: validEmailAddress_2.py
Name: Tony
----------------------------
Please construct your own feature vectors
and try to surpass the accuracy achieved by
Jerry's feature vector in validEmailAddress.py.
v feature1: no '@' in the str
v feature2: '.'in the first letter or previous one letter of @
v feature3: No strings before '@' no strings after '@'
v feature4: before@ not have any alphabets
v feature5: There is '..' after '@'
v feature6: There is no white space
v feature7: Ends with '.com' or '.edu' or '.tw'
v feature8: have'"' before one letter of @
v feature9: have'"' before @ but not before one letter of @
v feature10: There is ".." but not have '"'  before @

Accuracy of your model: 1.0
"""

import numpy as np
WEIGHT = [                           # The weight vector selected by you
	[-1.5],                              # (Please fill in your own weights)
	[-1.5],
	[-1.5],
	[-1.5],
	[-1.5],
	[0.5],
	[0.2],
	[0.3],
	[-1.5],
	[-1.5]
]

DATA_FILE = 'is_valid_email.txt'     # This is the file name to be processed


def main():
	maybe_email_list = read_in_data()
	line = 0
	accurate = 0
	for maybe_email in maybe_email_list:
		line += 1
		feature_vector = np.array(feature_extractor(maybe_email))
		weight_vector = np.array(WEIGHT).T
		score = weight_vector.dot(feature_vector)
		if score <= 0 and line <= 13:
			accurate += 1
		if score > 0 and line > 13:
			accurate += 1
	print(str(accurate / len(maybe_email_list)))


def feature_extractor(maybe_email):
	"""
	:param maybe_email: str, the string to be processed
	:return: list, feature vector with value 0's and 1's
	"""
	feature_vector = [0] * len(WEIGHT)
	for i in range(len(feature_vector)):
		if i == 0:
			feature_vector[i] = 1 if '@' not in maybe_email else 0
		elif i == 1:
			if feature_vector[0] == 0 and '@' != maybe_email[0]:
				feature_vector[i] = 1 if'.' in maybe_email[0] or '.' == maybe_email.split('@')[0][-1] else 0
		elif i == 2:
			if feature_vector[0] == 0:
				feature_vector[i] = 1 if ' ' == maybe_email.split('@')[0] or '\n' == maybe_email.split('@')[1] else 0
		elif i == 3:
			if feature_vector[0] == 0:
				alpha = 0
				for j in range(len(maybe_email.split('@')[0])):
					if maybe_email.split('@')[0][j].isalpha() or maybe_email.split('@')[0][j].isdigit():
						alpha += 1
					else:
						alpha += 0
				feature_vector[i] = 1 if alpha == 0 else 0
		elif i == 4:
			if feature_vector[0] == 0:
				feature_vector[i] = 1 if '..' in maybe_email.split('@')[1] else 0
		elif i == 5:
			feature_vector[i] = 1 if ' ' not in maybe_email else 0
		elif i == 6:
			feature_vector[i] = 1 if maybe_email[-5:] == '.com\n' or maybe_email[-5:] == '.edu\n' or \
									maybe_email[-4:] == '.tw\n' else 0
		elif i == 7:
			if feature_vector[0] == 0 and '@' != maybe_email[0]:
				feature_vector[i] = 1 if '"' in maybe_email.split('@')[0][-1] else 0
		elif i == 8:
			if feature_vector[0] == 0 and '"' in maybe_email.split('@')[0] and not feature_vector[7]:
				feature_vector[i] = 1
		elif i == 9:
			if feature_vector[0] == 0:
				feature_vector[i] = 1 if '..' in maybe_email.split('@')[0] and '"' not in maybe_email.split('@')[0] else 0
	return feature_vector


def read_in_data():
	"""
	:return: list, containing strings that may be valid email addresses
	"""
	maybe_email_list = []
	with open(DATA_FILE, "r") as f:
		for line in f:
			maybe_email_list.append(line)
	return maybe_email_list


if __name__ == '__main__':
	main()
