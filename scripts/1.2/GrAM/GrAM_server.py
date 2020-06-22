# GrAM_server.py                                        Phillipe Gauvin-Bourdon
'''
This script contain the visualization element for the testing of GrAM module. 
The grid environnement is represented in an internet page. 
'''
# --------------------------IMPORT PACKAGES------------------------------------
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule
from GrAM_main import GrAM
from GrAM_agent import Grazers, Grass, Shrub

# --------------------------SERVER FUNCTIONS-----------------------------------

width = 100
height = 100

def grazer_portrayal(agent):

    if agent is None:
        raise TypeError("There are no agents on the grid")

    portrayal = {"Shape": "rect",
                "Filled": "True",
                "w":0.8, "h": 0.8,
                "Layer": 0}

    if type(agent) is Grass:
        portrayal["Layer"] = 0
        if agent.biomass > 0.6:
            portrayal["Color"] = "#31a354"
        elif agent.biomass > 0.3:
            portrayal["Color"] = "#a1d99b"
        else:
            portrayal["Color"] = "#e5f5e0"

    if type(agent) is Shrub:
        portrayal["Shape"] = "circle"
        portrayal["r"] = 0.8
        portrayal["Layer"] = 1
        if agent.biomass > 0.6:
            portrayal["Color"] = "#6E2C00"
        elif agent.biomass > 0.3:
            portrayal["Color"] = "#DC7633"
        else:
            portrayal["Color"] = "#EDBB99"

    if type(agent) is Grazers:
        portrayal["Shape"] = "circle"
        portrayal["Color"] = "#AA0000"
        portrayal["r"] = 0.5
        portrayal["Layer"] = 2
        portrayal["text"] = agent.unique_id
        portrayal["text_color"] = "Yellow"
        
    return portrayal

canvas_element = CanvasGrid(grazer_portrayal, width, height, canvas_width=500, canvas_height=500)
chart_element = ChartModule([{"Label": "Grass biomass", "Color": "#31a354"},
                            {"Label": "Shrub biomass", "Color": "#6E2C00"}])
model_param = {"width": width, "height": height, "num_grazer": 10, "dens_grass": 0.35}

server = ModularServer(GrAM, [canvas_element, chart_element], "GrAM", model_param)
server.launch()