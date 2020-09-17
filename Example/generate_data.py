from .sudoku import Sudoku
import numpy as np

def generate_xy(num_samples, dim):
    X, Y = [], []
    for _ in range(num_samples):
        s = Sudoku(dimension=dim)
        Y.append(s.get_board_image())
        sol = s.create_empty_entries()
        X.append(s.get_board_image())
    return np.array(X), np.array(Y)

def generate_data(num_train, num_valid, num_test, dimension=2):
    X_train, Y_train = generate_xy(num_train, dimension)
    #X_train = X_train.reshape(len(X_train), dimension, dimension, 1)
    X_valid, Y_valid = generate_xy(num_valid, dimension)
    #X_valid = X_valid.reshape(len(X_valid), dimension, dimension, 1)
    X_test, Y_test = generate_xy(num_test, dimension)
    #X_test = X_test.reshape(len(X_test), dimension, dimension, 1)
    return X_train, Y_train, X_valid, Y_valid, X_test, Y_test