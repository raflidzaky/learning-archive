import pytest
import numpy as np
from sklearn.linear_model import LinearRegression
from basic_ml_pipeline import RegressionModel

# Different from previous "test_logic.py" which uses unittest
# This module uses pytest framework

# Basically, both test unit function
# The difference is, pytest needs no class (just direct function to test specific part of a function)
# Also, unittest needs an entry point (if __name__ == "__main__": unittest.main()) to collect all of the test case
# To partially check specific function, just call the method (for unittest) or pytest -k test_* (for pytest)

# Initialize the data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 2, 3, 4, 5])

# Initialize the model
model = RegressionModel(LinearRegression(), X, y)
X_train, X_test, y_train, y_test = model.train_test()

def test_split():
    # This func input is X/y train and test
    # The end goal is to make sure whether it really splits out the data AND
    # it splits accordingly (correct size)

    # Define test case for train dataset
    count_x_train = len(X_train)
    count_x       = len(X)
    total_x       = count_x_train / count_x

    count_y_train = len(y_train)
    count_y       = len(y)
    total_y       = count_y_train / count_y

    assert total_x == pytest.approx(0.8)
    assert total_y == pytest.approx(0.8)

    # Define test case for test dataset
    count_x_test = len(X_test)
    total_xs     = count_x_test / count_x

    count_y_test = len(y_test)
    total_ys     = count_y_test / count_y

    assert total_xs == pytest.approx(0.2)
    assert total_ys == pytest.approx(0.2)

def test_fitting():
    # Fit the model
    model.fit(X_train, y_train)
    
    # After fitting, check if the model has been trained and coefficients are updated
    assert model.model.coef_ is not None
    assert model.model.intercept_ is not None

def test_prediction():
  # Test model prediction
  # Since it is kinda basic (and rather deterministic number), it should return good in favor
    prediction = model.predict(X_test=[[7]])
    assert prediction == pytest.approx(8, rel=1)
