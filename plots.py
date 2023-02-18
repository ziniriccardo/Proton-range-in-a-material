# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 14:28:05 2022

@author: ricky
"""

import numpy as np
import matplotlib.pylab as plt

import sys
import configparser

configu = configparser.ConfigParser()
configu.read(sys.argv[1])

source0= configu.get('paths', 'stop_powers')
source1=configu.get('paths', 'positions')
source2=configu.get('paths','energies')

image_destination= configu.get('paths','plot_pic')
image_destination_1=configu.get('paths','plot_pic_1')
material=configu.get('values','material')

def make_plots():   
    
    stop_powers=np.load(source0)
    positions=np.load(source1)
    energies=np.load(source2)
    
    #Bragg_Peak plot
    fig,ax = plt.subplots()
    
    ax.plot(positions,stop_powers,label= material)
    
    ax.set_xlabel('Range (g/cm**2)') 
    ax.set_ylabel('-dE/dx (MeV cm**2 /g)') 

    ax.legend(loc='upper center')
      
    plt.savefig(image_destination)
    
    #Energy plot
    fig,ax = plt.subplots()
    
    ax.plot(positions,energies,label= material)
    
    ax.set_xlabel('Range (g/cm**2)') 
    ax.set_ylabel('Energy (MeV \cm g**-1)') 
    
    ax.legend(loc='upper right')
    
    plt.savefig(image_destination_1)
 
make_plots()
print("Image plots saved:"+ image_destination+ ' and '+ image_destination_1)

