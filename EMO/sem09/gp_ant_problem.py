"""
This example is from "John R. Koza. Genetic Programming: On the Programming 
of Computers by Natural Selection. MIT Press, Cambridge, MA, USA, 1992.".
The problem is called The Artificial Ant Problem. 
<http://www.cs.ucl.ac.uk/staff/w.langdon/bloat_csrp-97-29/node2.html>
The goal of this example is to show how to use DEAP and its GP framework with
with complex system of functions and object. 
Given an AntSimulator ant, this solution should get the 89 pieces of food
within 543 moves.
ant.routine = ant.if_food_ahead(ant.move_forward, prog3(ant.turn_left, 
                                                  prog2(ant.if_food_ahead(ant.move_forward, ant.turn_right), 
                                                        prog2(ant.turn_right, prog2(ant.turn_left, ant.turn_right))),
                                                  prog2(ant.if_food_ahead(ant.move_forward, ant.turn_left), ant.move_forward)))
Best solution found with DEAP:
prog3(prog3(move_forward, 
            turn_right, 
            if_food_ahead(if_food_ahead(prog3(move_forward,
                                              move_forward, 
                                              move_forward), 
                                        prog2(turn_left, 
                                              turn_right)), 
                          turn_left)), 
      if_food_ahead(turn_left, 
                    turn_left), 
      if_food_ahead(move_forward, 
                    turn_right)) 
fitness = (89,)
"""

import sys
import copy
import random
import time

import numpy

from functools import partial

from deap import algorithms
from deap import base
from deap import creator
from deap import tools
from deap import gp

import pygame

"""
Helper Functions
"""
def progn(*args):
    for arg in args:
        arg()

def prog2(out1, out2): 
    return partial(progn,out1,out2)

def prog3(out1, out2, out3):     
    return partial(progn,out1,out2,out3)

def if_then_else(condition, out1, out2):
    out1() if condition() else out2()

"""
The Ant Simulator
Modified to record moves 
"""
class AntSimulator(object):
    direction = ["north","east","south","west"]
    dir_row = [1, 0, -1, 0]
    dir_col = [0, 1, 0, -1]
    
    def __init__(self, max_moves):
        self.max_moves = max_moves
        self.moves = 0
        self.eaten = 0
        self.routine = None
        self.recorded_moves = []
        
    def _reset(self):
        self.row = self.row_start 
        self.col = self.col_start 
        self.dir = 1
        self.moves = 0  
        self.eaten = 0
        self.matrix_exc = copy.deepcopy(self.matrix)
        self.recorded_moves = []

    def record_move(self):
        self.recorded_moves.append(self.position)

    @property
    def position(self):
        return (self.row, self.col, self.direction[self.dir])
            
    def turn_left(self): 
        if self.moves < self.max_moves:
            self.moves += 1
            self.dir = (self.dir - 1) % 4
            self.record_move()

    def turn_right(self):
        if self.moves < self.max_moves:
            self.moves += 1    
            self.dir = (self.dir + 1) % 4
            self.record_move()
        
    def move_forward(self):
        if self.moves < self.max_moves:
            self.moves += 1
            self.row = (self.row + self.dir_row[self.dir]) % self.matrix_row
            self.col = (self.col + self.dir_col[self.dir]) % self.matrix_col
            if self.matrix_exc[self.row][self.col] == "food":
                self.eaten += 1
            self.matrix_exc[self.row][self.col] = "passed"
            self.record_move()

    def sense_food(self):
        ahead_row = (self.row + self.dir_row[self.dir]) % self.matrix_row
        ahead_col = (self.col + self.dir_col[self.dir]) % self.matrix_col        
        return self.matrix_exc[ahead_row][ahead_col] == "food"
   
    def if_food_ahead(self, out1, out2):
        return partial(if_then_else, self.sense_food, out1, out2)
   
    def run(self,routine):
        self._reset()
        while self.moves < self.max_moves:
            routine()
    
    def parse_matrix(self, matrix):
        self.matrix = list()
        for i, line in enumerate(matrix):
            self.matrix.append(list())
            for j, col in enumerate(line):
                if col == "#":
                    self.matrix[-1].append("food")
                elif col == ".":
                    self.matrix[-1].append("empty")
                elif col == "S":
                    self.matrix[-1].append("empty")
                    self.row_start = self.row = i
                    self.col_start = self.col = j
                    self.dir = 1
        self.matrix_row = len(self.matrix)
        self.matrix_col = len(self.matrix[0])
        self.matrix_exc = copy.deepcopy(self.matrix)

def run():

    ant = AntSimulator(600)

    def evalArtificialAnt(individual):
        # Transform the tree expression to functionnal Python code
        routine = gp.compile(individual, pset)
        # Run the generated routine
        ant.run(routine)
        return ant.eaten,

    pset = gp.PrimitiveSet("MAIN", 0)
    pset.addPrimitive(ant.if_food_ahead, 2)
    pset.addPrimitive(prog2, 2)
    pset.addPrimitive(prog3, 3)
    pset.addTerminal(ant.move_forward)
    pset.addTerminal(ant.turn_left)
    pset.addTerminal(ant.turn_right)

    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()

    # Attribute generator
    toolbox.register("expr_init", gp.genFull, pset=pset, min_=1, max_=2)

    # Structure initializers
    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr_init)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)



    toolbox.register("evaluate", evalArtificialAnt)
    toolbox.register("select", tools.selTournament, tournsize=7)
    toolbox.register("mate", gp.cxOnePoint)
    toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
    toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)
    random.seed(69)
    
    with  open("santafe_trail.txt") as trail_file:
      ant.parse_matrix(trail_file)
    
    pop = toolbox.population(n=300)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)
    
    algorithms.eaSimple(pop, toolbox, 0.5, 0.2, 100, stats, halloffame=hof)

    hofpt = gp.PrimitiveTree(hof[0])
    routine = gp.compile(hofpt, pset)
    ant.run(routine)
    # return pop, hof, stats
    return ant
    
def visualise(ant):
    grid = ant.matrix
    direction = ["north","east","south","west"]
    
    width, height = len(grid[0]), len(grid)
    
    food_pos = {}
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 'food':
                food_pos[(i, j)] = True

    cur_pos = (ant.row_start, ant.col_start, direction[ant.dir])
    moves = ant.recorded_moves

    print(moves)
    cur_move = -1

    cell_size = 30

    pygame.init()
    
    clock = pygame.time.Clock()
    size = (width*cell_size, height*cell_size)
    
    bgcolor = 245, 245, 220
    antimg = pygame.image.load("ant.png")
    foodimg = pygame.image.load("food.png")

    screen = pygame.display.set_mode(size)
    hold_for_rec = True

    while 1:
        if hold_for_rec:
            time.sleep(10)
            hold_for_rec = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        # clear screen
        screen.fill(bgcolor)

        # eat food
        if (cur_pos[0], cur_pos[1]) in food_pos:
            food_pos[(cur_pos[0], cur_pos[1])] = False

        # place food
        for food_coord, alive in food_pos.items():
            if alive:
                screen.blit(pygame.transform.scale(foodimg, (28, 28)), (1 + food_coord[1]*cell_size, 1 + food_coord[0]*cell_size))

        # move ant
        ant_screen = pygame.transform.scale(antimg, (28, 28))
        if cur_pos[2] == "east":
            ant_screen = pygame.transform.rotate(ant_screen, -90)
        elif cur_pos[2] == "north":
            ant_screen = pygame.transform.rotate(ant_screen, 180)
        elif cur_pos[2] == "west":
            ant_screen = pygame.transform.rotate(ant_screen, 90)

        screen.blit(ant_screen, (1 + cur_pos[1]*cell_size, 1 + cur_pos[0]*cell_size))
        
        cur_move += 1
        if cur_move < len(moves):
            cur_pos = moves[cur_move]
        pygame.display.flip()
        print(cur_pos)
        clock.tick(15)

if __name__ == "__main__":
    ant = run()
    visualise(ant)