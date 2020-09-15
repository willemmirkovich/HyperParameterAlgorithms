from .Population import Population
from .helpers import weighted_probability_choice

class Simple:

    def __init__(self, shape):
        self.shape = shape

    def fit(self, X_train, Y_train, X_valid, Y_valid, epochs):
        None

    def evaluate(self, X_test, Y_test):
        None

def test_basic():
    p = Population(2)
