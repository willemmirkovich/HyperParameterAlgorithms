from numpy.random import choice

def weighted_probability_choice(population):
    probs = []
    total = 0
    for i in range(population.size):
        fitness = population.get_fitness(i)
        probs.append(fitness)
        total += fitness
    new_total = 0
    for i in range(len(probs)):
        probs[i] = probs[i]/total
        new_total += probs[i]
    for i in range(len(probs)):
        probs[i] = probs[i]/new_total
    print(sum(probs))
    choices = choice(list(range(population.size)), size=2, p=probs)
    return choices[0], choices[1]

def find_min(curr_min, value):
    if value < curr_min:
        return value