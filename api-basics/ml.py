import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Create and train a simple model
class RegressionModel():
    def __init__(self, model, X, y):
        self.model = model
        self.X = X
        self.y = y
    
    def train_test(self):
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, 
                                                            test_size=0.2, 
                                                            random_state=1)
        return X_train, X_test, y_train, y_test
    
    def fit(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)

