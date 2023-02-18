# Proton Range in a material

## Proton traversing material simlation 
The following code  makes a calculation of the proton range in a given material using Bethe Bloch formula; input variables are needed to properly compute the formula: initial energy of the proton, the target material and its properties: density (rho), ratio betweeen proton and neutron (Z_over_A), ionization energy(e_ioniz) and number of protons (Z). In this way any type of material can be choose as target. In the example reported a 100 MeV proton into a carbon beam was used.

Once parameters are given the main function computes all quantities needed to compute the Stoopping Power using Bethe Bloch formula.
At the end final value of energy loss is set to zero when the proton stops in the material; a correction is made in the final part of the path to make clearer the Bragg-Peak.
The energy and the lenght step are set and the range calculation is finally made. 
As a reference two plots are produced in fucntion of the range: the Stopping Power and the energy of the proton.


## How make calculation
The steps needed to run the code and plot the results are:

1-Install all the necessary libraries using the preferred installer (like pip or conda). The libraries used in this code are numpy, configparser,  os, sys and matplotlib.

2-Launch the file [compile_bragg.py](/compile_bragg.py) which imports required paramteters from [materials.txt](/materials.txt) using configparser library: insert 'python compile.py materials.txt' in the command line. Input parameters can be modified choosing a different target material with its corresponding properties. The resulting data are saved in the data folder using their local paths.

3-Finally, launch the plot file plot.py using the same configuration: 'python plot.py materials.txt' in the command line. Through their local paths data are load from materials.txt and the plots are saved in the **plot** folder. 

## Project Structure
The project is divided into different files

•	In [bragg_peak.py](/bragg_peak.py) there is the main function which compute Bethe Bloch, ranges and energies values. After its execution arrays are saved for analysis.

•	In [testing.py](/testing.py) are present few tests for the main function in order to control cases with special input parameters and control result of range for a known case.

•	In [materials.txt](/materials.txt) there are all input parameters for particle and target material and local paths for the array data and for the plots. To make the example a 100 MeV proton into a Carbon target was choosen.

•	In [compile_bragg.py](/compile_bragg.py) there is the main part of the simulation: it computes the main function using parameters in input from materials.txt file. And a final terminal output which confirms that all worked properly printing out the result.

•	In [plot.py](/plot.py) there are the two final plots settings. Stopping power and energy in function of range of the particle. Using configparser data are loaded form the saved arrays.

Final plots for a proton energy of 100 MeV:

![](/images/bragg_peak.png) ![](/images/energy.png)
