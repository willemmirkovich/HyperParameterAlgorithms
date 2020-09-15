import numpy as np

from .Population import Population
from .helpers import weighted_probability_choice, find_min

# TODO crete better name than Model
# TODO better name for fitness function
def genetic_algorithm(model, X_train, Y_train, X_valid, Y_valid, X_test, Y_test,
                      size=50, generations=3, mutation_probability=.1, epochs=30, fitness_function=None):

    shape = X_train[0].shape

    choose_function = weighted_probability_choice

    # TODO Check shape of data and model works out

    # init population
    p = Population(size)
    for _ in size:
        member = model(shape)
        member.generate_random_model()
        idx = p.add(member)
        # TODO compile this before I think
        member.fit(X_train, Y_train, X_valid, Y_valid, epochs)
        fitness = member.evaluate(X_test, Y_test)
        p.set_fitness(idx, fitness)

    # TODO minimize/maximize

    for _ in generations:

        temp = Population(size)

        # TODO possilby parameterize? can't tell yet with tf optimizations
        for _ in size:

            # pick 2 members based on method of selection
            idx_one, idx_two = choose_function(p)
            p_one, p_two = p.get_member(idx_one), p.get_member(idx_two)

            # create new member based on parents
            member = model()
            args = get_args(p_one, p_two, mutation_probability)
            member.generate_model(args)
            idx = temp.add(member)
            # TODO possibly compile
            member.fit(X_train, Y_train, X_valid, Y_valid, epochs)
            fitness = member.evaluate(X_test, Y_test)
            temp.set_fitness(idx, fitness)

        p = temp

    # find best member of last generation
    if not fitness_function:
        fitness_function = find_min
    curr_value = p.get_fitness(0)
    idx = 0
    for i in range(p.size):
        value = fitness_function(curr_value, p.get_fitness(i))
        if (value != curr_value):
            idx = i

    return p.get_member(idx)
    # for debug, can return whole population

def get_args(p_one, p_two, mutation_probability):
    r = len(p_one.arg_choices)
    split = np.random.randint(0, r)
    p_one_args = p_one.args[:split]
    p_two_args = p_two.args[split:]
    args = p_one_args + p_two_args
    mutate = np.random.choice([True, False], p=[mutation_probability, 1-mutation_probability])
    if mutate:
        idx = np.random.choice(list(range(len(args))))
        args[idx] = np.random.choice(p_one.arg_choices[idx]['values'])
    return args
