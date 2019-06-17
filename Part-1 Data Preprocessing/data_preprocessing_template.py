# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 13:40:55 2019

@author: Aishwarya
"""

#importing libraries
import numpy as np                #contains mathematical tools
import matplotlib.pyplot as plt   #plot charts
import pandas as pd               #import and manage datasets


#importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

'Used only when some data is missing'
'Taking care of missing data'
"""from sklearn.preprocessing import Imputer 
imputer=Imputer(missing_values='NaN', strategy='mean', axis=0)
imputer=imputer.fit(X[:, 1:3])
X[:, 1:3]=imputer.transform(X[:, 1:3])"""

'Used only when encoding of the categorical data is required'
'Encoding categorical data'
"""from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:,0]=labelencoder_X.fit_transform(X[:, 0])
onehotencoder=OneHotEncoder(categorical_features=[0])
X=onehotencoder.fit_transform(X).toarray()
labelencoder_y = LabelEncoder()
y = labelencoder_X.fit_transform(y)"""

#Splitting the dataset into the training se and test set'
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

'Used if the libraries do not apply feature scaling'
#Feature scaling
"""from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""