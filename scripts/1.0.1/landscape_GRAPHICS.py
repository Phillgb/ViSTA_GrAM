from landscape_SETUP import *
from matplotlib import colors
from matplotlib.ticker import MaxNLocator

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*- MAIN *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

def plot_wind_figures (windspeed_dataset, total_sand_vol, total_aval_vol, initial_sand_heights_grid, sand_heights_grid, windspeed_grid, w_soil_moisture_grid):

    #Plot windspeed
    plt.figure(0); plt.plot(wind_time, windspeed_dataset)
    plt.xlabel("Years"); plt.ylabel("Wind velocity (m/s)"); plt.title("Wind velocity")
    plt.grid(b=True, which="both", axis='both')
    plt.tight_layout()
    plt.savefig('./windspeed_Timeserie.png', dpi=300)

    #Plot eroded volume
    plt.figure(1); plt.subplot(1,2,1); plt.plot(wind_time, total_sand_vol, color='C1')
    plt.plot([0, 0],[0, 1.05],color="white")
    plt.xlabel("Years"); plt.ylabel("Volume (m^3)"); plt.title("Erosion volume")
    plt.grid(b=True, which='both', axis='both')
    
    #Plot avalanching volume
    plt.subplot(1,2,2); plt.plot(wind_time, total_aval_vol, color='C1')
    plt.plot([0, 0],[0, 1.05],color="white")
    plt.xlabel("Years"); plt.ylabel("Volume (m^3)"); plt.title("Avalanching volume")
    plt.grid(b=True, which='both', axis='both')
    plt.tight_layout()
    plt.savefig('./ErodAvalVol_fig.png', dpi=300)
    
    #Plot sand heights, initial and final
    # Create a discrete colormap for sediment height
    YlOrBr = cm.get_cmap('YlOrBr', 5)
    sed_cmap = colors.ListedColormap(YlOrBr(np.linspace(0, 1, 5, endpoint=True)))
    sed_cmap.set_bad('0.5')
    sed_cmap.set_over('0.0')
    cbar_ticks = np.linspace(0, 2.5, 6, endpoint=True)
    
    plt.figure(2); plt.subplot(1,2,1)
    plt.imshow(initial_sand_heights_grid, cmap=sed_cmap, interpolation='none', origin='lower')
    plt.title("Initial sand heights")
    plt.colorbar()
    plt.subplot(1,2,2)
    plt.imshow(sand_heights_grid, cmap=sed_cmap, interpolation='none', origin='lower')
    plt.title("Final sand heights")
    plt.clim(0, 2.5)
    plt.colorbar(ticks=cbar_ticks, extend='max')
    plt.tight_layout()
    plt.savefig('./SandHeight_fig.png', dpi=300)
    
    #Plot final windspeed and moisture
    Greys = cm.get_cmap('Greys', 5)
    wind_cmap = colors.ListedColormap(Greys(np.linspace(0, 1, 5, endpoint=True)))
    wind_cmap.set_under('r', alpha=0.4)
    wind_ticks = np.linspace(0, np.max(windspeed_grid)-windspeed_threshold, 6, endpoint=True)

    plt.figure(3); plt.subplot(1,2,1)
    plt.imshow(windspeed_grid - windspeed_threshold, cmap=wind_cmap, interpolation='none', origin='lower')
    plt.title("Final windspeed grid")
    plt.clim(0, np.max(windspeed_grid)-windspeed_threshold)
    plt.colorbar(ticks=wind_ticks)
    plt.subplot(1,2,2)
    plt.imshow(w_soil_moisture_grid, cmap='Blues', interpolation='none', origin='lower')
    plt.clim(0, 1.0)
    plt.title("Final moisture grid")
    plt.colorbar()
    plt.tight_layout()
    plt.savefig('./WindspeedMoist_fig.png', dpi=300)

    # Close all open figures
    plt.close('all')
    
def plot_veg_figures (initial_veg_grid, veg_grid, initial_apparent_veg_type_grid, apparent_veg_type_grid, porosity_grid, age_grid, walls_grid, interaction_field, total_veg_pop, average_age_table, veg_proportions, rainfall_series, exposed_wall_proportions, veg_growth_factor):
    # Isolating each vegetation type in veg_grid
    iso_initial_veg_grid = np.zeros(3).astype(np.object)
    iso_veg_grid = np.zeros(3).astype(np.object)

    iso_initial_veg_grid[0] = np.zeros((Nr, Nc))
    iso_initial_veg_grid[0][np.where(initial_apparent_veg_type_grid == 1)] = initial_veg_grid[np.where(initial_apparent_veg_type_grid == 1)]
    iso_veg_grid[0] = np.zeros((Nr, Nc))
    iso_veg_grid[0][np.where(apparent_veg_type_grid == 1)] = veg_grid[np.where(apparent_veg_type_grid == 1)]
    
    iso_initial_veg_grid[1] = np.zeros((Nr, Nc))
    iso_initial_veg_grid[1][np.where(initial_apparent_veg_type_grid == 2)] = initial_veg_grid[np.where(initial_apparent_veg_type_grid == 2)]
    iso_veg_grid[1] = np.zeros((Nr, Nc))
    iso_veg_grid[1][np.where(apparent_veg_type_grid == 2)] = veg_grid[np.where(apparent_veg_type_grid == 2)]   
    
    iso_initial_veg_grid[2] = np.zeros((Nr, Nc))
    iso_initial_veg_grid[2][np.where(initial_apparent_veg_type_grid == 3)] = initial_veg_grid[np.where(initial_apparent_veg_type_grid == 3)]
    iso_veg_grid[2] = np.zeros((Nr, Nc))
    iso_veg_grid[2][np.where(apparent_veg_type_grid == 3)] = veg_grid[np.where(apparent_veg_type_grid == 3)]
    
    #Plot veg heights, initial and final
    # Grass grid
    # Create discrete colormap for grass height
    BuGn = cm.get_cmap('BuGn', 4)
    grass_cmap = colors.ListedColormap(BuGn(np.linspace(0, 1, 4, endpoint=True)))
    grass_cmap.set_bad('0.5')
    grass_ticks=np.linspace(0, max_height_grass, 5, endpoint=True)
    
    plt.figure(4); plt.subplot(3,2,1)
    plt.imshow(np.ma.masked_equal(iso_initial_veg_grid[0], 0), cmap=grass_cmap, interpolation='none', origin='lower')
    plt.colorbar(ticks=grass_ticks); plt.clim(0, max_height_grass)
    plt.title("Initial veg heights for grass")
    plt.subplot(3,2,2)
    plt.imshow(np.ma.masked_equal(iso_veg_grid[0], 0), cmap=grass_cmap, interpolation='none', origin='lower')
    plt.colorbar(ticks=grass_ticks); plt.clim(0, max_height_grass)
    plt.title("Final veg heights for grass")
    
    # Shrub grid
    # Create discrete colormap for shrub height
    shrub_cmap = colors.ListedColormap(BuGn(np.linspace(0, 1, 4, endpoint=True)))
    shrub_cmap.set_bad('0.5')
    shrub_ticks = np.linspace(0, max_height_shrub, 5, endpoint=True)

    plt.subplot(3,2,3)
    plt.imshow(np.ma.masked_equal(iso_initial_veg_grid[1], 0), cmap=shrub_cmap, interpolation='none', origin='lower')
    plt.colorbar(ticks=shrub_ticks); plt.clim(0, max_height_shrub)
    plt.title("Initial veg heights for shrub")
    plt.subplot(3,2,4)
    plt.imshow(np.ma.masked_equal(iso_veg_grid[1], 0), cmap=shrub_cmap, interpolation='none', origin='lower')
    plt.colorbar(ticks=shrub_ticks); plt.clim(0, max_height_shrub)
    plt.title("Final veg heights for shrub")
    
    # Tree grid
    # Create discrete colormap for tree height
    BuGn = cm.get_cmap('BuGn', 6)
    tree_cmap = colors.ListedColormap(BuGn(np.linspace(0, 1, 6, endpoint=True)))
    tree_cmap.set_bad('0.5')
    tree_ticks = np.linspace(0, max_height_tree, 7, endpoint=True)

    plt.subplot(3,2,5)
    plt.imshow(np.ma.masked_equal(iso_initial_veg_grid[2], 0), cmap=tree_cmap, interpolation='none', origin='lower')
    plt.colorbar(ticks=tree_ticks); plt.clim(0, max_height_tree)
    plt.title("Initial veg heights for tree")
    plt.subplot(3,2,6)
    plt.imshow(np.ma.masked_equal(iso_veg_grid[2], 0), cmap=tree_cmap, interpolation='none', origin='lower')
    plt.colorbar(ticks=tree_ticks); plt.clim(0, max_height_tree)
    plt.title("Final veg heights for tree")
    
    plt.tight_layout()
    plt.savefig('./VegHeight_fig.png', dpi=300)
    
    #Plot probability of survival 
    plt.figure(5); plt.subplot(1, 2, 1); plt.imshow(interaction_field, cmap='OrRd', interpolation='none', origin='lower'); plt.colorbar(); plt.clim(0, 1); plt.title('Neighbourhood stress')
    plt.subplot(1, 2, 2); plt.imshow(age_grid, cmap='BuGn', interpolation='none', origin='lower'); plt.colorbar(); plt.clim(0, 300); plt.title('Plant age')
    plt.tight_layout()
    plt.savefig('./ProbSurvival_fig.png', dpi=300)

    #Plot vegetation type
    # Create a discrete colormap for vegetation figures 
    veg_cmap = colors.ListedColormap(['white', '#a6cee3', '#1f78b4', '#b2df8a'])
    veg_bounds = [-0.5, 0.5, 1.5, 2.5, 3.5]
    veg_ticks = [0, 1, 2, 3]

    plt.figure(6); plt.subplot(1,2,1)
    plt.imshow(initial_apparent_veg_type_grid, cmap=veg_cmap, interpolation='none', origin='lower'); plt.clim(0, 3); plt.title("Initial veg types"); plt.colorbar(cmap=veg_cmap, boundaries=veg_bounds, ticks=veg_ticks)
    plt.subplot(1,2,2)
    plt.imshow(apparent_veg_type_grid, cmap=veg_cmap, interpolation='none', origin='lower'); plt.clim(0, 3); plt.title("Final veg types"); plt.colorbar(cmap=veg_cmap, boundaries=veg_bounds, ticks=veg_ticks)
    plt.tight_layout()
    plt.savefig('./VegType_fig.png', dpi=300)

    #Plot walls grid
    plt.figure(7); plt.imshow(walls_grid, cmap='RdBu', interpolation='none', origin='lower'); plt.colorbar(); plt.title('Solid walls')
    plt.tight_layout()
    plt.savefig('./Walls_fig.png', dpi=300)
    
    #Plot population change
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    line1, = ax1.plot(np.append(0, veg_time), np.append(veg_distrib, total_veg_pop/(Nr*Nc)), color='C2')
    line2, = ax2.plot(veg_time, rainfall_series, color='C0')
    ax1.set_xlabel('Years')
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
    ax4.plot(veg_time, average_age_table[:, 0], color='#a6cee3')
    ax4.plot(veg_time, average_age_table[:, 1], color='#1f78b4')
    ax4.plot(veg_time, average_age_table[:, 2], color='#b2df8a')
    ax4.set_xlabel('Years')
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
    ax5.plot(np.append(0, veg_time), np.append(grass_proportion, veg_proportions[:, 0]), color='#a6cee3')
    ax5.plot(np.append(0, veg_time), np.append(shrub_proportion, veg_proportions[:, 1]), color='#1f78b4')
    ax5.plot(np.append(0, veg_time), np.append(tree_proportion, veg_proportions[:, 2]), color='#b2df8a')
    ax5.set_xlabel('Years')
    ax5.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax5.set_ylabel('Proportion of total veg cover', color='k')
    plt.legend(['Grass', 'Shrub', 'Tree'])
    ax5.set_ylim([0, 1.05])
    plt.title("Plant proportions")
    ax5.grid(b=True, which='both', axis='both')
    plt.tight_layout()
    plt.savefig('./VegProport_TimeSerie.png', dpi=300)
   
    #Close all open figures
    plt.close('all')
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-