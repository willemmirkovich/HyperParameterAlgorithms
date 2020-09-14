from .sudoku import Sudoku
import numpy as np

def generate_xy(num_samples, board_dim, tile_dim):
    X, Y = [], []
    for _ in range(num_samples):
        s = Sudoku(board_dimension=board_dim, tile_dimension=tile_dim)
        val = s.create_empty_entries()
        X.append(s.board)
        Y.append(np.array([val]))
    return X, Y

def generate_data(num_train, num_valid, num_test, board_dim=3, tile_dim=3):
    X_train, Y_train = generate_xy(num_train, board_dim, tile_dim)
    X_valid, Y_valid = generate_xy(num_valid, board_dim, tile_dim)
    X_test, Y_test = generate_xy(num_test, board_dim, tile_dim)
    return X_train, Y_train, X_valid, Y_valid, X_test, Y_test