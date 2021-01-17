import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import pypickle as clk
import warnings
warnings.filterwarnings('ignore')


def hello(X_test3):
	data = pd.read_csv('soil_fertility.csv')
	data1 = data.drop(data[data['fertility'] == 2].index)
	df = data1
	X = df.iloc[:,:-1]
	y = df.iloc[:,-1]
	X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=6)

	num_columns = ['N','P','K','ph','ec']
	normalizer = MinMaxScaler()
	normalizer.fit(X_train[num_columns])
	X_train[num_columns] = normalizer.transform(X_train[num_columns])
	filename='fertility_model.pkl'
	loaded_model = clk.load(filename,'rb')

	X_test4 = normalizer.transform(X_test3)

	y_pred3 = loaded_model.predict(X_test4)
	return int(y_pred3)