import pytest
import numpy as np
from sklearn.linear_model import LinearRegression
from ml import RegressionModel
import pickle

# Initialize the data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 2, 3, 4, 5])

# Initialize the model
model = RegressionModel(LinearRegression(), X, y)
X_train, X_test, y_train, y_test = model.train_test()

# Fit the model
model.fit(X_train, y_train)

# Serialize the model
with open('trained_model.pkl', 'wb') as file:
    pickle.dump(model, file)
  
