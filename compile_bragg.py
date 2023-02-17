# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 16:47:18 2022

@author: ricky
"""

import bragg_peak as bp

import numpy as np

import configparser

import os
import sys

##some calculation for obtain energy.

config = configparser.ConfigParser()
config.read(sys.argv[1])


os.makedirs('./data',exist_ok=True)
os.makedirs('./plots',exist_ok=True)

destination0= config.get('paths', 'stop_powers')
destination1=config.get('paths','positions')
destination2=config.get('paths','energies')


energies= int(config.get('values','energies'))
particle=config.get('values','particle')
material= config.get('values','material')


rho= float(config.get('values','rho'))
Z_over_A= float(config.get('values', 'Z_over_A'))    
e_ioniz= float(config.get('values', 'e_ioniz'))
Z=int(config.get('values', 'Z'))


mat_properties=[rho,Z_over_A,e_ioniz,Z]


#for i in range(0,len(energies)):
 
    
plot_vectors=bp.compute_bethe_bloch(particle,energies,material,mat_properties)
   
#plot_vectors_1=bp.compute_bethe_bloch('pion',100,'carbon')
#ave figures plot
np.save(destination0, plot_vectors[0])
np.save(destination1,plot_vectors[1])
np.save(destination2,plot_vectors[2])



if   len(plot_vectors[0])!=0 and len(plot_vectors[1])!=0 :
    print("Simulation Done: \n")

    print('For a ' +particle+ ' of energy',energies, ' MeV in ' + material+'\n')

    print ('Range ' , plot_vectors[1][plot_vectors[4]-1]/mat_properties[0], 'cm , ' , plot_vectors[1][plot_vectors[4]-1], 'g/cm**2')

else: print("Particle of 0 MeV has range 0 cm.")
  
  
