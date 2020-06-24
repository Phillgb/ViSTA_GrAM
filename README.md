# ViSTA_GrAM
------------------------------------------------------------------------------------------------------------------------------------------------------
## Description

The ViSTA_GrAM model simulate the influence of grazing in arid and semi-arid environment as a spacially process. The model integrate an agent-based module, representing individual grazers, to an 
already established cellular automaton ViSTA (Mayaud et al., 2017), representing the vegetation and sediment transport processes. The coupling of vegetation, sediment transport and grazing
interactions offer an integrative and informative representation of the arid and semi-arid environment. 

The three main module of the model (managing vegetation, sediment transport and grazing) communicate with each other to inform the evolution of their respectives components 
based on the state of their environments. The vegetation can then influence the amount of sediment transport occuring on the grid by limiting the wind speed on the surface and 
in return the sediment transport can influence the vegetation growth by limiting or increasing the suplement of nutrient to the vegetation via aeolian transport. The grazing module 
is also directly influencing the vegetation coverage via the foraging of grazers and a decrease in vegetation coverage can in turn also increase the sediment transport. The behavior of 
the grazers is influenced by both the vegetation and the sediment transport trough five factors (1. Biomass availability, 2. Presence of obstacle, 3. Sediment surface slopes, 4. Memory of visited cells).
The grazers will move to a cell of their choice and than forage in a Moore neigbourhood around their position at each iterations observing a grazing activity.

For more information regarding the application of the model, please see the open-source publication cited bellow (Gauvin-Bourdon et al., 2020).

## Usage

The ViSTA_GrAM model is executed from the landscape_MAIN.py script, which in turn coordinate the communication between each modules. The user inputs to the model 
are given via the landscape_SETUP.py file. The GrAM module being built-in the ViSTA model, it only need to be enable or disabled via modifications made to the landscape_SETUP.py file
like any other parameter of the model.

## Dependency

The ViSTA_GrAM model is written in Python 3.7.7.

The main packages used by the model are: 
    
    - Scipy
    - Numpy
    - Matplotlib
    - Mesa

A requirement.txt file is also disponible to help create an environment in which the model can be executed and have its outputs analysed.

------------------------------------------------------------------------------------------------------------------------------------------------------
## Copyright note: 

The ViSTA model on which this module is based was developped by Jerome R. Mayaud, Richard M. Bailey and Giles F.S. Wiggs.
The original code of the ViSTA model is available in Jerome Mayaud GitHub repository: https://github.com/jeromemayaud/ViSTA.git.

The development of the grazing agent module (GrAM) and the adaptation of the ViSTA model to this new module was done by Phillipe Gauvin-Bourdon.

## Reference
1. Gauvin-Bourdon, P., King, J., Perez, L. (2020). Integration of a grazing agent-based model in the modelling of sand transport and vegetation growth interactions. Under review
2. Mayaud, J. R., Bailey, R. M. & Wiggs, G. F. S. (2017). A coupled vegetation/sediment-transport model for dryland environments. Journal of Geophysical Research: Earth Surface. doi:10.1002/2016JF004096