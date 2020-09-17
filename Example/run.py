from GeneticAlgorithm import genetic_algorithm

from .generate_data import generate_data

from .NN import NN

X_train, Y_train, X_valid, Y_valid, X_test, Y_test = generate_data(200, 50, 50, dimension=3)

best_candidate = genetic_algorithm(NN, X_train, Y_train, X_valid, Y_valid, X_test, Y_test,
                                   epochs=30, generations=3, size=20)

best_candidate.save()



