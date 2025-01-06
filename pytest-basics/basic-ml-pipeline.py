import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Now, jump in to apply unit testing on basic ML pipeline

# Create and train a simple model pipeline 
# (including model init, train-test split, training model, testing model)
class RegressionModel():
    def __init__(self, model, X, y):
      # Initialize model and input
        self.model = model
        self.X = X
        self.y = y
    
    def train_test(self):
      # Train and test method using train_test_split as a helper
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, 
                                                            test_size=0.2, 
                                                            random_state=1)
        return X_train, X_test, y_train, y_test
    
    def fit(self, X_train, y_train):
      # Train model
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
      # Return a prediction
        return self.model.predict(X_test)
