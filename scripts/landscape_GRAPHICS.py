from landscape_SETUP import *
from matplotlib import colors
from matplotlib.ticker import MaxNLocator 

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*- SETUP *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
#Creating a minimized "Paired" colormap for vegetation figures 
veg_cmap = colors.ListedColormap(['white', '#a6cee3', '#1f78b4', '#b2df8a'])
veg_bounds = [-0.5, 0.5, 1.5, 2.5, 3.5]
veg_ticks = [0, 1, 2, 3]

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*- MAIN *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

def plot_wind_figures (windspeed_dataset, total_sand_vol, total_aval_vol, initial_sand_heights_grid, sand_heights_grid, windspeed_grid, w_soil_moisture_grid):

    #Plot windspeed
    plt.figure(0); plt.plot(windspeed_dataset)
    plt.xlabel("Wind iterations"); plt.ylabel("Wind velocity (m/s)"); plt.title("Wind velocity")
    plt.grid(b=True, which="both", axis='both')
    plt.tight_layout()
    plt.savefig('./windspeed_Timeserie.png', dpi=300)

    #Plot eroded volume
    plt.figure(1); plt.subplot(1,2,1); plt.plot(total_sand_vol, color='C1')
    plt.plot([0, 0],[0, 1.05],color="white")
    plt.xlabel("Wind iterations"); plt.ylabel("Volume (m^3)"); plt.title("Erosion volume")
    plt.grid(b=True, which='both', axis='both')
    
    #Plot avalanching volume
    plt.subplot(1,2,2); plt.plot(total_aval_vol, color='C1')
    plt.plot([0, 0],[0, 1.05],color="white")
    plt.xlabel("Wind iterations"); plt.ylabel("Volume (m^3)"); plt.title("Avalanching volume")
    plt.grid(b=True, which='both', axis='both')
    plt.tight_layout()
    plt.savefig('./ErodAvalVol_fig.png', dpi=300)
    
    #Plot sand heights, initial and final
    plt.figure(2); plt.subplot(1,2,1)
    plt.imshow(initial_sand_heights_grid, cmap='YlOrBr', interpolation='none'); plt.title("Initial sand heights"); plt.colorbar()
    plt.subplot(1,2,2)
    plt.imshow(sand_heights_grid, cmap='YlOrBr', interpolation='none'); plt.title("Final sand heights"); plt.colorbar()
    plt.tight_layout()
    plt.savefig('./SandHeight_fig.png', dpi=300)
    
    #Plot final windspeed and moisture
    plt.figure(3); plt.subplot(1,2,1)  
    plt.imshow(windspeed_grid, cmap='Greys', interpolation='none'); plt.title("Final windspeed grid"); plt.colorbar()
    plt.subplot(1,2,2)
    plt.imshow(w_soil_moisture_grid, cmap='Blues', interpolation='none'); plt.clim(0, 1.0); plt.title("Final moisture grid"); plt.colorbar()
    plt.tight_layout()
    plt.savefig('./WindspeedMoist_fig.png', dpi=300)

    # Close all open figures
    plt.close('all')
    
def plot_veg_figures (initial_veg_grid, veg_grid, initial_apparent_veg_type_grid, apparent_veg_type_grid, porosity_grid, age_grid, walls_grid, interaction_field, total_veg_pop, average_age_table, veg_proportions, rainfall_series, exposed_wall_proportions):
    #Plot veg heights, initial and final 
    plt.figure(4); plt.subplot(1,2,1)
    plt.imshow(initial_veg_grid, cmap='BuGn', interpolation='none'); plt.colorbar(); plt.clim(0, 6.0); plt.title("Initial veg heights") 
    plt.figure(4); plt.subplot(1,2,2)
    plt.imshow(veg_grid, cmap='BuGn', interpolation='none'); plt.colorbar(); plt.clim(0, 6.0); plt.title("Final veg heights")
    plt.tight_layout()
    plt.savefig('./VegHeight_fig.png', dpi=300) 
    
    #Plot probability of survival 
    plt.figure(5); plt.subplot(1, 2, 1); plt.imshow(interaction_field, cmap='OrRd', interpolation='none'); plt.colorbar(); plt.clim(0, 1); plt.title('Neighbourhood stress')
    plt.subplot(1, 2, 2); plt.imshow(age_grid, cmap='BuGn', interpolation='none'); plt.colorbar(); plt.clim(0, 300); plt.title('Plant age')
    plt.tight_layout()
    plt.savefig('./ProbSurvival_fig.png', dpi=300)

    #Plot vegetation type
    plt.figure(6); plt.subplot(1,2,1)
    plt.imshow(initial_apparent_veg_type_grid, cmap=veg_cmap, interpolation='none'); plt.clim(0, 3); plt.title("Initial veg types"); plt.colorbar(cmap=veg_cmap, boundaries=veg_bounds, ticks=veg_ticks)
    plt.subplot(1,2,2)
    plt.imshow(apparent_veg_type_grid, cmap=veg_cmap, interpolation='none'); plt.clim(0, 3); plt.title("Final veg types"); plt.colorbar(cmap=veg_cmap, boundaries=veg_bounds, ticks=veg_ticks)
    plt.tight_layout()
    plt.savefig('./VegType_fig.png', dpi=300)

    #Plot walls grid
    plt.figure(7); plt.imshow(walls_grid, cmap='RdBu', interpolation='none'); plt.colorbar(); plt.title('Solid walls')
    plt.tight_layout()
    plt.savefig('./Walls_fig.png', dpi=300)
    
    #Plot population change
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    time = np.arange(0, veg_iterations)
    line1, = ax1.plot(time, (total_veg_pop/(Nr*Nc)), color='C2')
    line2, = ax2.plot(time, rainfall_series, color='C0')
    ax1.set_xlabel('Vegetation iterations')
    ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax1.set_ylabel('Population density')
    ax2.set_ylabel('Precipitation (annual equivalent, mm)')
    ax1.set_ylim([0, 1])   
    plt.title("Population density and precipitation")
    ax1.grid(b=True, which='both', axis='both')
    ax2.grid(b=True, which='both', axis='both', color='#c0c0c0', linestyle='--')
    plt.legend((line1, line2), ('Vegetation population density', 'Precipitation'))
    plt.tight_layout()
    plt.savefig('./Popdens_Timeserie.png', dpi=300)
    
    #Plot alpha vs population
    fig, ax3 = plt.subplots()
    ax3.plot(rainfall_series, (total_veg_pop/(Nr*Nc)), color='C0', marker='o', ls='None'); ax3.invert_xaxis()
    ax3.set_xlabel("Precipitation (annual equivalent, mm)"); ax3.set_ylabel("Population density")
    ax3.set_ylim([0, 1])
    ax3.xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.title("Population density vs precipitation")
    ax3.grid(b=True, which='both', axis='both')
    plt.tight_layout()
    plt.savefig('./PopDensPrecip_fig.png', dpi=300)
    
    #Plot average age
    fig, ax4 = plt.subplots()
    ax4.plot(time, average_age_table[:, 0], color='#a6cee3')
    ax4.plot(time, average_age_table[:, 1], color='#1f78b4')
    ax4.plot(time, average_age_table[:, 2], color='#b2df8a')
    ax4.set_xlabel('Vegetation iterations')
    ax4.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax4.set_ylabel('Average plant age', color='k')
    plt.legend(['Grass', 'Shrub', 'Tree'])
    ax4.set_ylim([0, 1000])
    ax4.grid(b=True, which='both', axis='both')
    plt.title("Average age")
    plt.tight_layout()
    plt.savefig('./VegAge_Timeserie.png', dpi=300)
    
    #Plot veg type proportions
    fig, ax5 = plt.subplots()
    ax5.plot(time, veg_proportions[:, 0], color='#a6cee3')
    ax5.plot(time, veg_proportions[:, 1], color='#1f78b4')
    ax5.plot(time, veg_proportions[:, 2], color='#b2df8a')
    ax5.set_xlabel('Vegetation iterations')
    ax5.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax5.set_ylabel('Proportion of total veg cover', color='k')
    plt.legend(['Grass', 'Shrub', 'Tree'])
    ax5.set_ylim([0, 1.05])
    plt.title("Plant proportions")
    ax5.grid(b=True, which='both', axis='both')
    plt.tight_layout()
    plt.savefig('./VegProport_TimeSerie.png', dpi=300)
    
    #Plot wall exposures
    plt.figure(); plt.plot(exposed_wall_proportions)
    plt.plot([0, 0],[0, 1.05],color="white")
    plt.xlabel("Model iterations"); plt.ylabel("% of exposed walls"); plt.title("Exposed walls")
    plt.grid(b=True, which='both', axis='both')
    plt.tight_layout()
    plt.savefig('./WallExpo_fig.png', dpi=300)
   
    #Close all open figures
    plt.close('all')

def plot_grazing_figure(grazing_heat_map, mean_travel_array):
    # Plot the map of grazer passage on the grid cell
    plt.figure(); plt.imshow(grazing_heat_map, cmap="OrRd", interpolation=None)
    plt.colorbar()
    plt.title("Grazer passage intensity (number of passage)")
    plt.tight_layout()
    plt.savefig('./grazer_heat_map.png', dpi=300)

    # Plot timeserie of mean distance traveled per each grazing event
    plt.figure(); ax6 = plt.gca()
    plt.plot(mean_travel_array)
    plt.xlabel('Vegetation iterations')
    ax6.xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.ylabel('Mean distance traveled (m)')
    plt.title('Mean distance traveled each time a grazing agent move')
    plt.grid(b=True, which='both', axis='both')
    plt.tight_layout()
    plt.savefig('./dist_travel_timeserie.png', dpi=300)

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-