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
    


##Spread ou Bragg Peak-SOBP.
###out only one value in energies vector!

'''

if len(energies)>1: print ("only one value needed in energies vector")

sobp_stop_powers=np.empty(len(plot_vectors[0][2]))
sobp_positions=np.ndarray(len(plot_vectors[0][4]))
color_mat=''
sobp_vectors=[]

energies_bp=np.linspace(50,60,100)

for i in range(0,len(energies_bp)):
    single_bp_0=bp.compute_bethe_bloch(beam,energies_bp[i],material)
    single_bp_1=bp.compute_dose(single_bp_0)
    #if len(single_bp_1)==len(sobp_stop_powers):
    sobp_stop_powers+=single_bp_1[2]
    sobp_positions=single_bp_1[4]
    color_mat=single_bp_1[7]
        
    #else: continue   
    
sobp_vectors.append(sobp_stop_powers)
sobp_vectors.append(sobp_positions)
sobp_vectors.append(material)
sobp_vectors.append(color_mat)

plots.make_bp_plots(sobp_vectors)
'''