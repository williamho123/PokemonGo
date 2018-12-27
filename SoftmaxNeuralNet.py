from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
import keras.utils
import numpy as np
import OneHotConversion as oh

def BuildModelFromData(filename):
	model = Sequential()
	model.add(Dense(256, activation='sigmoid', input_dim=152))
	model.add(Dropout(0.2))
	model.add(Dense(256, activation='sigmoid'))
	model.add(Dropout(0.2))
	model.add(Dense(256, activation='sigmoid'))
	model.add(Dropout(0.2))
	model.add(Dense(21, activation='softmax'))

	model.compile(optimizer='adagrad', loss='categorical_crossentropy', metrics=['accuracy'])
	raw_data = oh.GenerateDataAndLablesFromCsv(filename)
	np.random.shuffle(raw_data)
	data = raw_data[:,:152]
	labels = raw_data[:,152:153]
	labels = keras.utils.to_categorical(labels, num_classes =21)
	train_data = (data)[:210000,:]
	train_labels = labels[:210000,:]
	test = (data)[210000:,:]
	test_labels = labels[210000:,:]

	model.fit(train_data,train_labels, epochs= 50, batch_size = 128, verbose=2)
	score = model.evaluate(test, test_labels, batch_size = 128)
	print(score)

BuildModelFromData('./data/DataV6.csv')
