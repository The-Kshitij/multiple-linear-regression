# -*- coding: utf-8 -*-
"""ML_linear_regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dvEmxafOAl86Ze9BHnTNJoVYUdULT0Xb
"""

'''
aim: to predict the weight of the fish.
'''
import pandas as pd;
import numpy as np;

from sklearn.compose import ColumnTransformer;
from sklearn.preprocessing import OneHotEncoder;

from sklearn.model_selection import train_test_split;

from sklearn.preprocessing import StandardScaler;

from sklearn.linear_model import LinearRegression;

import matplotlib.pyplot as plt;

dataset = pd.read_csv("Fish.csv");

print(dataset)

print(dataset.shape);

x = np.append(dataset.iloc[:,2:].values,dataset.iloc[:,0].values.reshape(len(dataset.iloc[:,0]),1),axis=1);

y = dataset.iloc[:,1].values;

print(y)

print(x)

#for encoding the categorical values in x
ct = ColumnTransformer(transformers=[("encoder",OneHotEncoder(),[-1])],remainder="passthrough");

x = np.array(ct.fit_transform(x));

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=1);

#for feature scaling
Scaler = StandardScaler();

#can fit the scaling only on the training set as that are the values that we will have and also
#starting from 3 as the first 3 values are encoded values of categorical values
Scaler.fit(x_train[:,3:]);
x_train[:,3:] = Scaler.transform(x_train[:,3:]);

x_test[:,3:] = Scaler.transform(x_test[:,3:]);

print(x_train);

print(x_test);

'''
linear regression manages the dummy variable trap and also takes into acount the constant
value.
'''
Regressor = LinearRegression();

Regressor.fit(x_train,y_train);

y_pred = Regressor.predict(x_test);

np.printoptions(precision=2);
output = np.concatenate((y_pred.reshape(len(y_pred),1),y_test.reshape(len(y_test),1)),1);

prc=0;
for i in range(0,len(output)):
    if (prc==0):
        plt.scatter(i,output[i][0],color="blue",marker="*",label="predicted");
        plt.scatter(i,output[i][1],color="red",label="actual");
        prc=1;
    else:
        plt.scatter(i,output[i][0],color="blue",marker="*");
        plt.scatter(i,output[i][1],color="red");

plt.ylabel("Weight of the fish");
plt.xlabel("Values");
plt.legend();
plt.show();