from numpy.random import choice

def weighted_probability_choice(population):
    probs = []
    total = 0
    for i in range(population.size):
        fitness = population.get_fitness(i)
        probs.append(fitness)
        total += fitness
    max_v = max(probs)
    min_v = min(probs)
    for i in range(len(probs)):
        probs[i] = max_v + min_v - probs[i]
    new_total = 0
    for i in range(len(probs)):
        probs[i] = probs[i]/total
        new_total += probs[i]
    for i in range(len(probs)):
        probs[i] = probs[i]/new_total
    choices = choice(list(range(population.size)), size=2, p=probs)
    return choices[0], choices[1]

def find_min(curr_min, value):
    if value < curr_min:
        return value

def plot_avg_fitness(fitness_history):
    None

def equal_weight_fitness(validation_loss, test_loss):
    # TODO: need to fix this to include validation loss as well
    return (.5(test_loss) + .5(validation_loss))

# TODO add method here to plot some history stats