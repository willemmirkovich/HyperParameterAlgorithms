import numpy as np

from tqdm import tqdm

from .Population import Population
from .helpers import weighted_probability_choice, find_min

# TODO crete better name than Model
# TODO better name for fitness function
def genetic_algorithm(model, X_train, Y_train, X_valid, Y_valid, X_test, Y_test,
                      size=50, generations=3, mutation_probability=.1, epochs=30, fitness_function=None):

    model(0)
    # TODO make more generic for all use
    input_shape = X_train[0].shape

    choose_function = weighted_probability_choice

    # TODO Check shape of data and model works out

    # init population
    p = Population(size)

    print('Generating Initial Population')
    for _ in tqdm(range(size)):
        member = model(input_shape)
        member.generate_random_model()
        idx = p.add(member)
        member.fit(X_train, Y_train, X_valid, Y_valid, epochs)
        fitness = member.evaluate(X_test, Y_test)
        p.set_fitness(idx, fitness)


    # TODO plot performance over each generation
    for g in range(generations):
        print('\n')
        print('Generation ' + str(g) + '\n')


        temp = Population(size)

        # TODO possilby parameterize? can't tell yet with tf optimizations
        for _ in tqdm(range(size)):

            # pick 2 members based on method of selection
            idx_one, idx_two = choose_function(p)
            p_one, p_two = p.get_member(idx_one), p.get_member(idx_two)

            # create new member based on parents
            member = model(input_shape)
            parameters = get_parameters(p_one, p_two, mutation_probability)
            member.generate_model(parameters)
            idx = temp.add(member)
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

def get_parameters(p_one, p_two, mutation_probability):
    r = len(p_one.parameter_choices)
    split = np.random.randint(0, r)
    p_one_parameters = p_one.parameters[:split]
    p_two_parameters = p_two.parameters[split:]
    parameters = p_one_parameters + p_two_parameters
    mutate = np.random.choice([True, False], p=[mutation_probability, 1-mutation_probability])
    if mutate:
        idx = np.random.choice(list(range(len(parameters))))
        parameters[idx] = np.random.choice(p_one.parameter_choices[idx]['values'])
    return parameters
