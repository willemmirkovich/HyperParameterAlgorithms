import numpy as np

class Sudoku:

    def __init__(self, dimension=2):
        self.dimension=dimension
        self.board=self.__generate_board()
        self.__create_valid_game()

    def solve(self):
        grid = self.board.copy()
        res, sol = self.__rec_solve(grid)
        self.board = sol

    def print(self):
        for row in range(len(self.board)):
            text = ''
            text += '| '
            for col in range(len(self.board[row])):
                text += str(int(self.board[row][col])) + ' '
                if col % self.dimension == (self.dimension - 1):
                    text += '| '
            print(text)
            count = len(text)
            if row % self.dimension == (self.dimension - 1):
                print(count*'-')

    def create_empty_entries(self, num_entries=1):
        sol = self.__generate_board()
        idx = list(range(self.dimension * self.dimension))
        choices = []
        while len(choices) != num_entries:
            choice = [np.random.choice(idx), np.random.choice(idx)]
            if choice not in choices:
                choices.append(choice)
        for choice in choices:
            sol[choice[0]][choice[1]] = self.board[choice[0]][choice[1]]
            self.board[choice[0]][choice[1]] = 0
        return sol

    def get_board_image(self):
        # image[height][width] = value
        return self.board.reshape(self.dimension * self.dimension,
                                  self.dimension * self.dimension, 1)

    # should get rid of this
    def load_from_image(self, image):
        self.board = image.reshape(self.dimension * self.dimension,
                                   self.dimension * self.dimension)

    def __generate_board(self):
        board = []
        for _ in range(self.dimension*self.dimension):
            temp = []
            for _ in range(self.dimension*self.dimension):
                temp.append(0)
            board.append(temp)
        return np.array(board)

    def __create_valid_game(self):
        self.solve()

    def __is_full(self, grid):
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if grid[row][col] == 0:
                    return False
        return True

    def __rec_solve(self, grid):
        if self.__is_full(grid):
            return True, grid
        vals = range(1, len(self.board) + 1)
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if grid[row][col] == 0:
                    vals = list(np.random.choice(vals, size=len(vals), replace=False))
                    while True:
                        if len(vals) != 0:
                            val = vals.pop()
                            temp = grid.copy()
                            temp[row][col] = val
                            if self.__check_col(temp, col) \
                                    and self.__check_row(temp, row)\
                                    and self.__check_square(temp, (row-(row % self.dimension)), (col-(col % self.dimension))):
                                res, sol = self.__rec_solve(temp)
                                if res:
                                    return True, sol
                        else:
                            return False, None

    def __check_square(self, grid, start_row, start_col):
        used = []
        for row in range(self.dimension):
            for col in range(self.dimension):
                val = grid[start_row+row][start_col+col]
                if val == 0:
                    continue
                if val in used:
                    return False
                used.append(val)
        return True

    def __check_row(self, grid, row):
        used = []
        for col in range(len(self.board[row])):
            val = grid[row][col]
            if val == 0:
                continue
            if val in used:
                return False
            used.append(val)
        return True

    def __check_col(self, grid, col):
        used = []
        for row in range(len(self.board)):
            val = grid[row][col]
            if val == 0:
                continue
            if val in used:
                return False
            used.append(val)
        return True

    # TODO may be helpful for ml problems
    def __is_unique(self):
        None