from GeneticAlgorithm import genetic_algorithm
from Example.generate_data import generate_data
from Example.sudoku import Sudoku
from Example.NN import NN

X_train, Y_train, X_valid, Y_valid, X_test, Y_test = generate_data(200, 50, 50, dimension=3)

best_candidate = genetic_algorithm(NN, X_train, Y_train, X_valid, Y_valid, X_test, Y_test,
                                   epochs=50, generations=3, size=30)

best_candidate.save()

s = Sudoku(dimension=3)

print('Target')
s.print()

s.create_empty_entries()
test = s.get_board_image()
test = test.reshape((1, 9, 9, 1))
ans = best_candidate.model.predict(test)
ans.reshape((9, 9, 1))
s.load_from_image(ans)
print('Predict')
print(s.print())


