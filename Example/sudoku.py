import numpy as np

# TODO move this to its own git page
class Sudoku:

    def __init__(self, dimension=2):
        # TODO refactor code to comply with simple dimension argument
        self.b_dim=dimension
        self.t_dim=dimension
        self.board=self.__generate_board()
        self.__create_valid_game()

    def __generate_board(self):
        board = []
        for _ in range(self.b_dim*self.t_dim):
            temp = []
            for _ in range(self.b_dim*self.t_dim):
                temp.append(0)
            board.append(temp)
        return np.array(board)

    def __create_valid_game(self):
        # fill diags
        '''
        for i in range(self.b_dim):
                self.__fill_square(i * self.t_dim, i * self.t_dim)
        '''

        # next, fill remaining
        '''
        for i in range(self.b_dim):
            for j in range(self.b_dim):
                self.__fill_square(i * self.t_dim, j * self.t_dim, check=True)
        '''
        self.solve()

    # please dont be dumb

    def solve(self):
        grid = self.board.copy()
        res, sol = self.__rec_solve(grid)
        self.board = sol

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
                            print((row-(row % self.t_dim)))
                            print((col-(col % self.t_dim)))
                            if self.__check_col(temp, col) \
                                    and self.__check_row(temp, row)\
                                    and self.__check_square(temp, (row-(row % self.t_dim)), (col-(col % self.t_dim))):
                                res, sol = self.__rec_solve(temp)
                                if res:
                                    return True, sol
                        else:
                            return False, None

    def __check_square(self, grid, start_row, start_col):
        used = []
        for row in range(self.t_dim):
            for col in range(self.t_dim):
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

    # may be helpful for ml problems
    def __is_unique(self):
        None

    def print(self):
        for row in range(len(self.board)):
            text = ''
            text += '| '
            for col in range(len(self.board[row])):
                text += str(int(self.board[row][col])) + ' '
                if col % self.t_dim == (self.t_dim - 1):
                    text += '| '
            print(text)
            count = len(text)
            if row % self.t_dim == (self.t_dim - 1):
                print(count*'-')

    def create_empty_entries(self, num_entries=1):
        # TODO
        None

    def get_board_image(self):
        # image[height][width] = value
        return self.board

    # should get rid of this
    def load_from_image(self, image):
        self.board = image