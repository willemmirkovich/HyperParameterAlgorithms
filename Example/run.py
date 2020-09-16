from GeneticAlgorithm import genetic_algorithm

from .generate_data import generate_data

from .NN import NN

X_train, Y_train, X_valid, Y_valid, X_test, Y_test = generate_data(50, 30, 20)

best_candidate = genetic_algorithm(NN, X_train, Y_train, X_valid, Y_valid, X_test, Y_test,
                                   epochs=5, generations=1, size=5)

best_candidate.save()



