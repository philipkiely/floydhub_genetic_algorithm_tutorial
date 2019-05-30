# A genetic algorithm template

# imports

"""
# Overall Structure
initialize()
while(not termination_condition):
    fitness()
    selection()
    reproduce()
termination()
"""


# fitness_function evaluates an individual
def fitness_function(individual):
    return 0


# takes a function and list of arguments, applies function to arguments
def evaluate_generation(population):
    scores = []
    total = 0
    for individual in population:
        r = fitness_function(individual)
        scores.append(r)
        total += r
    avg = total / len(scores)
    return scores, avg


# Create child from parent
def mutate(individual):
    return individual


# given a population, return the best individual and the associated value
def find_best(population):
    best = None
    val = None
    for individual in population:
        r = fitness_function(individual)
        try:
            if r > val:
                best = individual
                val = r
        except: # On the first run, set the result as best
            best = individual
            val = r
    return best, val


# create a population of objects
def initialize():
    return []


# handle the output of the genetic algorithm
def termination(best, val):
    print(best, val)


# Main function runs when script is called
if __name__ == "__main__":
    population = initialize()
    iteration = 0
    total_iterations = 100
    for iteration in range(total_iterations): # main loop
        scores, avg = evaluate_generation(population) # run fitness function
        deleted = 0
        new_population = []
        for i in range(len(population)): # reproduce new generation
            if scores[i] < avg:
                deleted += 1
            else:
                new_population.append(population[i])
        for i in range(deleted):
            new_population.append(mutate(new_population[i % len(new_population)])) # iterate over population with overflow protection
        population = new_population
    best, val = find_best(population)
    termination()
