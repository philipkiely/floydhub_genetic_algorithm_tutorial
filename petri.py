# A genetic algorithm for simulating a population

import random
import sys


# A simple organism
class Organism():

    def __init__(self, cooperator):
        self.cooperator = cooperator
        self.energy = 1
        self.alive = True

    # if the organism is a cooperator, it will share energy
    def interact(self, population):
        if self.cooperator and self.alive:
            self.energy -= 1
            for i in range(8):
                population[random.randint(0, len(population) - 1)].energize()
        return population

    # increment energy every time energy is received
    def energize(self):
        self.energy += 1
        if random.randint(1, 50) == 1:
            self.alive = False

    # reproduce if possible
    def reproduce(self, population, population_size):
        if self.energy > 10 and self.alive and len(population) < population_size:
            self.energy -= 10
            population.append(Organism(self.cooperator))
        return population


# create a population of objects
def initialize(starting_cooperators, starting_noncooperators):
    population = []
    for i in range(starting_cooperators):
        population.append(Organism(True))
    for i in range(starting_noncooperators):
        population.append(Organism(False))
    return population


# fitness_function evaluates an individual
def fitness_function(individual):
    return individual.energy


# Adds one unit of energy to every organism
def add_energy(population):
    for individual in population:
        individual.energize()
    return population


# Let all cooperators cooperate
def interact(population):
    for individual in population:
        population = individual.interact(population)
    return population


# Remove dead organisms from the dish
def clean_dish(population):
    for individual in population:
        if not individual.alive:
            population.remove(individual)
    return population


# Let organisms reproduce if able
def reproduce(population, maximum_population):
    reproduction_order = sorted(population, key=lambda x: fitness_function(x), reverse=True)
    for individual in reproduction_order:
        population = individual.reproduce(population, maximum_population)
    return population


# handle the output of the genetic algorithm
def termination(population, starting_cooperators, starting_noncooperators, maximum_population, total_iterations):
    print("Ran", total_iterations, "generations in a dish with a capacity of", maximum_population)
    print("Beginning Population:")
    print("C" * starting_cooperators + "N" * starting_noncooperators)
    print("Ending Population")
    population_string = ""
    for individual in population:
        if individual.cooperator:
            population_string += "C"
        else:
            population_string += "N"
    print(population_string)


# Main function runs when script is called
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python petri.py coop noncoop max iter")
        exit()
    starting_cooperators = int(sys.argv[1])
    starting_noncooperators = int(sys.argv[2])
    maximum_population = int(sys.argv[3])
    if starting_cooperators + starting_noncooperators > maximum_population:
        print("maximum population less than starting population")
        exit()
    total_iterations = max(int(sys.argv[4]), 1) # must run for at least 1 iteration
    population = initialize(starting_cooperators, starting_noncooperators)
    for iteration in range(total_iterations):
        population = add_energy(population) # every organism generates energy
        population = interact(population) # energy is shared and consumed
        population = clean_dish(population) # remove dead organisms from the dish
        population = reproduce(population, maximum_population)
    termination(population, starting_cooperators, starting_noncooperators, maximum_population, total_iterations)
