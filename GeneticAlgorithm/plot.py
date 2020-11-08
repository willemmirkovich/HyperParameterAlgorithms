import matplotlib.pyplot as plt

def plot_fitness_history(history):
    # TODO: insert plots here for average fitness with CI interval over each generation
    for g in range(history):
        total_fitness = 0
        for m in range(history[g]):
            member_fitness = history[g][m]
            total_fitness = member_fitness + total_fitness
        average_fitness = total_fitness / len(history[g])

def plot_validation_loss_history(history):
    None

def plot_test_loss_history(history):
    None
        
        
