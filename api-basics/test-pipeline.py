import pytest
import numpy as np
from sklearn.linear_model import LinearRegression
from ml import RegressionModel

# Initialize the data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 2, 3, 4, 5])

# Initialize the model
model = RegressionModel(LinearRegression(), X, y)
X_train, X_test, y_train, y_test = model.train_test()

def test_X_type():
    # Test that X is a NumPy array
    assert isinstance(X, np.ndarray), f"Expected X to be a numpy.ndarray, but got {type(X)}"
    
def test_X_element_type():
    # Test that each element inside X is of type numpy.ndarray
    for i in X:
        for j in i:  # Iterate over each element in X (inner elements)
            assert isinstance(j, np.int64), f"Expected element in X to be np.int64, but got {type(j)}"

def test_y_type():
    # Test that X is a NumPy array
    assert isinstance(y, np.ndarray), f"Expected y to be a numpy.ndarray, but got {type(y)}"
    
def test_y_element_type():
    # Test that each element inside X is of type numpy.ndarray
    for i in y:
        assert isinstance(i, np.int64), f"Expected element in X to be np.int64, but got {type(y)}"

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
    prediction = model.predict(X_test=[[7]])
    assert prediction == pytest.approx(8, rel=1)

