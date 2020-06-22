#post_GRAPHICS.py                                       Phillipe Gauvin-Bourdon
#                    GRAPHIC CREATION AFTER RUN
'''
This script is aiming at allowing the recreation and reworking of graphics without
having to rerun the whole simulation each time.
'''
# ------------------------- IMPORT MODULES ------------------------------------
from landscape_SETUP import *
from landscape_GRAPHICS import *
from other_FUNCTIONS import startgrids, startgrids_2, startgrids_manual
import gc

# --------------------------- IMPORT DATA -------------------------------------
gc.collect() # Run garbage collector

actual_grazed_series = np.loadtxt('./Actual_grazing_amount.txt', delimiter=',')
age_grid = np.loadtxt('./Final_age_grid.txt', delimiter=',')
apparent_veg_type_grid = np.loadtxt('./Final_apparent_veg_grid.txt', delimiter=',')
avail_forage = np.loadtxt('./Forage_avail_series.txt', delimiter=',')
average_age_table = np.loadtxt('./Average_ages.txt', delimiter=',')
exposed_wall_proportions = np.loadtxt('./Exposed_wall_proportions.txt', delimiter=',')
grazer_passage_grid = np.loadtxt('./Grazing_heat_map_grid.txt', delimiter=',')
initial_sand_heights_grid = np.loadtxt('./Initial_sand_grid.txt', delimiter=',')
initial_veg_grid = np.loadtxt('./Initial_veg_grid.txt', delimiter=',')
initial_apparent_veg_type_grid = np.loadtxt('./Initial_veg_type_grid.txt', delimiter=',')
interaction_field = np.loadtxt('./Final_neighbourhood_stress.txt', delimiter=',')
rainfall_series = np.loadtxt('./Rainfall_series.txt', delimiter=',')
sand_heights_grid = np.loadtxt('./Final_sand_grid.txt', delimiter=',')
soil_moisture_grid = np.loadtxt('./Final_soil_moisture_grid.txt', delimiter=',')
total_aval_vol = np.loadtxt('./Total_aval_vol.txt', delimiter=',')
total_sand_vol = np.loadtxt('./Total_sand_vol.txt', delimiter=',')
total_veg_pop = np.loadtxt('./Veg_population.txt', delimiter=',')
veg_grid = np.loadtxt('./Final_veg_grid.txt', delimiter=',')
veg_growth_factor = np.loadtxt('./Veg_growth_series.txt', delimiter=',')
veg_growth_mass = np.loadtxt('./Vegetation_growth_amount.txt', delimiter=',')
veg_proportions = np.loadtxt('./Veg_proportions.txt', delimiter=',')
veg_type_grid = np.loadtxt('./Final_veg_type_grid.txt', delimiter=',')
windspeed_dataset = np.loadtxt('./Windspeed_series.txt', delimiter=',')
windspeed_grid = np.loadtxt('./Final_wind_grid.txt', delimiter=',')

startgrid2 = startgrids_2(veg_grid, veg_type_grid)
porosity_grid = startgrid2[0]
startgrid = startgrids()
walls_grid = startgrid[9]
# ---------------------------- PLOTTING ---------------------------------------

plot_wind_figures(windspeed_dataset, total_sand_vol, total_aval_vol, initial_sand_heights_grid, sand_heights_grid, windspeed_grid, soil_moisture_grid)
plot_veg_figures(initial_veg_grid, veg_grid, initial_apparent_veg_type_grid, apparent_veg_type_grid, porosity_grid, age_grid, walls_grid, interaction_field, total_veg_pop, average_age_table, veg_proportions, rainfall_series, exposed_wall_proportions, veg_growth_factor)

if grazing_event_timeseries == "GrAM":    
    plot_grazing_figure(grazer_passage_grid)