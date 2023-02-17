# Proton-range-in-a-material
Calculation of proton range in a material
The following code simulates the range of a proton traversing a given material using Bethe Bloch formula.
It first calculates energy loss for a given path through Bethe Bloch formula and its corrections.
Then, once defined the length step, associate to every position its corresponding value of energy loss. At the end final value of energy loss is set to zero when the proton stops in the material. A correction is made in the final part of the path to make clearer the Bragg-Peak.

How to run the Simulation
The steps needed to run the code and plot the results are:
1-	Install all the necessary libraries using the preferred installer (like pip or conda). The libraries used in this code are numpy, configparser,  os, sys and matplotlib.
2-	Launch the file compile.py which imports required paramteters form materials.txt using configparser library: “python compile.py materials.txt” in the command line. Input parameters can be modified choosing a different target material with its corresponding properties: density, proton/neutron ratio, ionization energy and number of protons. The resulting data are saved in the data folder using their local paths.
3-	Finally, launch the plot file plot.py using the same configuration:  “python plot.py materials.txt” in the command line. Through their local paths data are load from materials.txt and the plots are saved in the plot folder. 

Project Structure
The project is divided into different files
•	In bragg_peak.py there is the main function which compute Bethe Bloch, ranges and energies values. After its execution arrays are saved for analysis.
•	In testing,py are present few test for the main function in order to control cases for special input parameters and control result of range for a known case.
•	In materials.txt there are all input parameters for particle and target material and local paths for the array data and for plots.
•	In compile.py there is the …. Of the simulation computing the main function using parameters in input from materials.txt file. And a final text which confirms that all worked properly printing out the result.
•	In plot.py there are the two final plots settings. Stopping power and energy in function of range of the particle. Using configparser data are loaded form the saved arrays.
