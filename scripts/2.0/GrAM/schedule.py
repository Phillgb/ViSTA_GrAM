# schedule.py                                           Phillipe Gauvin-Bourdon
'''
This script is describing the scheduler for the GrAM module. This scheduler is 
making sure the agents are activated one type at the time. Each agents of the 
same type are activated at random. 
'''
# --------------------------IMPORT MODULES-------------------------------------

import random
from mesa.time import RandomActivation
from collections import defaultdict

# -----------------------RANDOM ACTIVATION BY BREED----------------------------
class RandomActivationByBreed(RandomActivation):
    ''' 
    A scheduler which activate each type of agent once per step, in random order,
    with the order reshuffled every step.

    This is inspired by MESA exemples WolfSheepPredation model and NetLogo 'ask
    breed' class.

    All agents must have a step() method.
    '''
    agents_by_breed = defaultdict(list)

    def __init__(self, model):
        super().__init__(model)
        self.agents_by_breed = defaultdict(list)

    def add(self, agent):
        '''
        Add an Agent object to the schedule

        Args:
            agent: An agent to be added to the schedule.
        '''

        self.agents.append(agent)
        agent_class = type(agent)
        self.agents_by_breed[agent_class].append(agent)

    def remove(self, agent):
        '''
        Remove all instances of a given agent from the schedule.
        '''

        while agent in self.agents:
            self.agents.remove(agent)

        agent_class = type(agent)
        while agent in self.agents_by_breed[agent_class]:
            self.agents_by_breed[agent_class].remove(agent)

    def step(self, by_breed=True):
        '''
        Executes the step of agent breed, one at a time, in random order.

        Args:
            by_breed: If True, run all agents of a single breed before running 
                      the next one.
        '''
        if by_breed:
            for agent_class in self.agents_by_breed:
                self.step_breed(agent_class)
            self.steps += 1
            self.time += 1
        else:
            super().step()

    def step_breed(self, breed):
        '''
        Shuffle order and run all agents of a given breed.

        Args:
            breed: Class objects of the breed to run.
        '''
        agents = self.agents_by_breed[breed]
        random.shuffle(agents)
        for agent in agents:
            agent.step()