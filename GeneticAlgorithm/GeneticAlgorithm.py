import numpy as np

from tqdm import tqdm

from time import perf_counter

from .Population import Population
from .helpers import weighted_probability_choice, find_min

# TODO crete better name than Model
# TODO better name for fitness function
# TODO maybe just pas x_train, y_train and give a validation split func
def genetic_algorithm(model, X_train, Y_train, X_valid, Y_valid, X_test, Y_test,
                      size=50, generations=3, mutation_probability=.1, epochs=30, fitness_function=None,
                      track_performance=False):

    if track_performance:
        start = perf_counter()

    input_shape = X_train[0].shape

    # TODO parameterize
    choose_function = weighted_probability_choice

    generation_history = []
    fitness_history = []
    generation_history.append([])
    fitness_history.append([])

    # init population
    p = Population(size)

    print('Generating Initial Population, 0')
    for _ in tqdm(range(size)):
        member = model(input_shape)
        member.generate_random_model()
        idx = p.add(member)
        generation_history[0].append(member.fit(X_train, Y_train, X_valid, Y_valid, epochs))
        fitness = member.evaluate(X_test, Y_test)
        fitness_history[0].append(fitness)
        p.set_fitness(idx, fitness)


    for g in range(generations):
        g_num = g + 1
        print('\n')
        print('Generation ' + str(g_num) + '\n')
        generation_history.append([])
        fitness_history.append([])

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
            generation_history[g_num].append(member.fit(X_train, Y_train, X_valid, Y_valid, epochs))
            fitness = member.evaluate(X_test, Y_test)
            fitness_history[g_num].append(fitness)
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

    if track_performance:
        end = perf_counter()
        t = end - start
        unit = 's'
        # choose unit based on time
        if t > 360:
            t = t / 60
            unit = 'm'
            if t > 60:
                t = t / 60
                unit = 'h'
        print('Execution time: {}{}'.format(t, unit))

    return p.get_member(idx), generation_history, fitness_history
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
