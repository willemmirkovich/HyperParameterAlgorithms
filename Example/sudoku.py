import numpy as np

# TODO move this to its own git page
class Sudoku:


    # TODO change data structure to image for simplicity
    def __init__(self, board_dimension=1, tile_dimension=3):
        self.b_dim=board_dimension
        self.t_dim=tile_dimension
        self.board=self.generate_board()
        self.create_valid_game()

    def generate_board(self):
        board = []
        for _ in range(self.b_dim):
            temp = []
            for _ in range(self.b_dim):
                temp.append(np.zeros((self.t_dim, self.t_dim)))
            board.append(temp)
        return np.array(board)

    def create_valid_game(self):
        for i in range(self.b_dim):
            for j in range(self.b_dim):
                r = self.t_dim ** 2
                # possible values for tiles
                nums = list(range(1, (r + 1)))
                # randomize each square on the board
                choices = []
                for x in range(0, self.t_dim):
                    for y in range(0, self.t_dim):
                        choices.append([x, y])
                choices = np.array(choices)
                np.random.shuffle(choices)
                choices = list(choices)
                for k in range(len(choices)):
                    self.board[i][j][choices[k][0]][choices[k][1]] = nums[k]

    def print(self):
        for cut in range(self.b_dim):
            for row in range(self.t_dim):
                # begin line
                text = ''
                text += '| '
                for line in range(self.b_dim):
                    for col in range(self.t_dim):
                        text += str(int(self.board[cut][line][row][col])) + ' '
                    text += '| '
                # end line
                print(text)
                count = len(text)
            print(count*'-')

    def create_empty_entries(self, num_entries=1):
        # TODO support more than one
        i = np.random.randint(0, self.b_dim)
        j = np.random.randint(0, self.b_dim)
        k = np.random.randint(0, self.t_dim)
        l = np.random.randint(0, self.t_dim)
        value = self.board[i][j][k][l]
        self.board[i][j][k][l] = 0
        return value

    def get_board_image(self):
        # image[height][width] = value
        return self.board.reshape(self.b_dim * self.t_dim, self.b_dim * self.t_dim, 1)

    # should get rid of this
    def load_from_image(self, image):
        # TODO DO NOT HARDCODE
        board = self.generate_board()
        for i in range(len(board)):
            for j in range(len(board[i])):
                for k in range(len(board[i][j])):
                    for l in range(len(board[i][j][k])):
                        board[i][j][k][l] = image[i+k][j+l]
        self.board = board