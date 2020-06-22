# GrAM_agent.py                                         Phillipe Gauvin-Bourdon
'''
This script is describing the agents populating the grid. 
'''
# -------------------------IMPORT PACKAGES-------------------------------------
import numpy as np
from mesa.agent import Agent
from mesa.datacollection import DataCollector

from landscape_SETUP import *
from wind_FUNCTIONS import wrap_grid, wrap_grid_2, unwrap_grid, unwrap_grid_2

# ------------------------GRAZERS AGENT----------------------------------------
class Grazers(Agent):
    # Setting initials parameters
    def __init__(self, unique_id, model, pos=None):
        super().__init__(unique_id, model)
        self.pos = pos
        self.pos_mem_grid = np.zeros((Nr, Nc)) # Create a grid representing the memory of the grazer for his past positions


    def decision(self):
        '''
        Decision making function on the next postion to adopt for the grazers 
        agents in the GrAM module.
        '''
        # Set initial parameters
        index = -1
        best_score = -np.inf
        best_pos = []

        # Wrap the sediment grid with margin cell to allow the calcul of slope on grid border
        if boundary_conditions == 'periodic':
            w_sand_grid = wrap_grid(self.model.sand_grid, 0)
        elif boundary_conditions == 'open':
            w_sand_grid = wrap_grid_2(self.model.sand_grid, 0)
    
        for r in range(Nr):
            for c in range(Nc):
                index += 1
                score = 0
                if isinstance(self.model.grid[c][r], Grazers): #Check if there is another grazer on the target cell the 
                    score -= 1.01
                
                # The vegetation need to be visible to influence the grazer decision of movement
                if self.model.veg_height_grid[r, c] > veg_threshold:
                    if self.model.veg_type_grid[r, c] == 1: # Check if Vegetation type of target cell is grass
                        if (self.model.veg_height_grid[r, c]/max_height_grass <= 0.75 and # Check if the height of vegetation on the grid is between 75% and 30% of maximum height for grass
                            self.model.veg_height_grid[r, c]/max_height_grass >= 0.3):  
                            score += 0.8
                        elif self.model.veg_height_grid[r, c]/max_height_grass <= 0.2: # Check if the height of the vegetation below 20% of the maximum height for grass
                            score += 0.4
                        else:
                            score += 0.6
 
                # Prevent the grazers will move on a wall cell
                if self.model.wall_grid[r, c] == 1:
                    score -= 1.01

                # Find the maximum height cell in the neighbourhood of the possible next cell
                max_height_sand = 0
                max_height_pos = np.zeros(2)
                min_height_sand = math.inf
                min_height_pos = np.zeros(2)

                for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        if w_sand_grid[r+dr, c+dc] > max_height_sand:
                            max_height_sand = w_sand_grid[r+dr, c+dc]
                            max_height_pos[0] = dr
                            max_height_pos[1] = dc

                        if w_sand_grid[r+dr, c+dc] < min_height_sand:
                            min_height_sand = w_sand_grid[r+dr, c+dc]
                            min_height_pos[0] = dr
                            min_height_pos[1] = dc
                
                # Find the angle of the slope on possible next cell
                dist = np.sqrt(np.power(max_height_pos[0]-min_height_pos[0], 2) + np.power(max_height_pos[1]-min_height_pos[1], 2))
                if dist == 0:
                    slope = 0
                else:
                    slope = (max_height_sand-min_height_sand) / (dist*cell_width) * 100

                # If the cell has a slope percentage above 25% (14.04°) remove chances to be choosed
                if slope > 25:
                    score -= 0.4
                
                # If the grazer already visited this place, it is more inclined to return there
                if self.pos_mem_grid[r, c] > 0:
                    score += 0.2

                # Evaluate if the score of the current cell is higher than the last 
                # best score and replace the score and next_position of the agent 
                # with the current if it is.
                if score > best_score:
                    best_score = score
                    best_pos = [(c, r)]
                elif score == best_score:
                    best_pos.append((c, r))

        return best_pos[np.random.choice(len(best_pos))]


    def move(self, new_pos):
        self.model.grid.move_agent(self, new_pos)
        self.pos_mem_grid[new_pos[1], new_pos[0]] += 1
        
        
    def eat(self):
        wx = grid_start + self.pos[0] # Addapt the x coordinate of the grazer position to corresponding coordinates in a wrapped grid
        wy = grid_start + self.pos[1] # Addapt the y coordinate of the grazer position to corresponding coordinates in a wrapped grid
        self.grazed_grid = np.zeros((Nrw, Ncw)) # Temporary grid representing the grazing done by the agent
        w_veg_height_grid = wrap_grid(self.model.veg_height_grid, 0) # Wrap vegetation height grid for eating process
        w_veg_type_grid = wrap_grid(self.model.veg_type_grid, 0) # Wrap vegetation type grid for eating process
        
        # Eating loop of a 2x2 cell area around the position of the grazer
        for dy in range(-2, 3):
            for dx in range(-2, 3):
                if w_veg_height_grid[wy+dy, wx+dx] > veg_threshold and w_veg_type_grid[wy+dy, wx+dx] == 1:
                    self.grazed_grid[wy+dy, wx+dx] += 0.03
                    self.model.passage_grid[wy+dy, wx+dx] += 1

        # Unwrap the grazing grid to match the size of original vegetation grid
        if boundary_conditions == 'periodic':
            self.grazed_grid = unwrap_grid(self.grazed_grid, 0)
        elif boundary_conditions == 'open':
            self.grazed_grid = unwrap_grid_2(self.grazed_grid, 0)

        self.model.veg_height_grid -= self.grazed_grid # Substract the amount of grazing done on the vegetation grid

    def step(self):
        new_position = self.decision() # Grazers make a decision on the best cell to move to,
        self.move(new_position) # than move to that cell,
        self.eat() # and than eat on that cell.