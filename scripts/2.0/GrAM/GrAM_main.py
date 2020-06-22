# GrAM_functions.py                                     Phillipe Gauvin-Bourdon                   
'''
This script contain the main function of the grazing agent model "GrAM" module,
creating each grazing agents, placing them on the grid and in the schedule 
before executing each step of the model. 
'''
# ------------------------IMPORTS PACKAGES-------------------------------------
import numpy as np
from mesa import Model
from mesa.time import RandomActivation
from mesa.space import SingleGrid
from mesa.datacollection import DataCollector

from GrAM.GrAM_agent import Grazers
from GrAM.schedule import RandomActivationByBreed
# ------------------------MAIN FUNCTION----------------------------------------

class GrAM(Model):
    ''' GrAM module main class. '''

    # Set initial parameters
    def __init__(self, grid_width, grid_height, height_grid, veg_type_grid, sand_grid, wall_grid, grazer_passage_grid, num_grazer):

        # Set parameters
        self.width = grid_width
        self.height = grid_height
        self.number_of_grazer = num_grazer
        self.veg_height_grid = height_grid
        self.veg_type_grid = veg_type_grid
        self.sand_grid = sand_grid
        self.wall_grid = wall_grid
        self.grazer_passage_grid = grazer_passage_grid
        self.grid = SingleGrid(self.width, self.height, torus=True)
        self.schedule = RandomActivationByBreed(self)

        # Create the agent grazers
        for i in range(self.number_of_grazer):
            grazer = Grazers(i, self)
            self.grid.position_agent(grazer)
            self.schedule.add(grazer)

        self.running = True

    def step(self):
        # Execute model step and collect data
        self.schedule.step()

    def run(self, n):
        '''Execute the model GrAM for "n" step'''
        for i in range(n):
            self.step()

        return self.veg_height_grid, self.veg_type_grid, self.grazer_passage_grid