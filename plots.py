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
        
    plt.subplots_adjust(left=0.1,bottom=0.1,right=0.9,top=0.9,wspace=0.3, hspace=0.4)
    plt.savefig(image_destination)
    
    #Energy plot
    fig,ax = plt.subplots()
    
    ax.scatter(positions,energies,label= material,s=2)
    
    ax.set_xlabel('Range (g/cm**2)') 
    ax.set_ylabel('Energy (MeV \cm g**-1)') 
    
    ax.legend(loc='upper right')

    #set distances between plots
    plt.subplots_adjust(left=0.1,bottom=0.1,right=0.9,top=0.9,wspace=0.3, hspace=0.4)
    plt.savefig(image_destination_1)
 
"""
def make_bp_plots(plots):
    fig,ax1 = plt.subplots()  
    stop_powers_1=plots[0]
    positions=plots[1]
    material=plots[2]
    color_mat=plots[3]
    
    ax1.plot(positions,stop_powers_1,label= material,color=color_mat)
    ax1.set_xlabel('range g/cm**"2') 
    ax1.set_ylabel('Dose Gy') 
    
    ax1.legend(loc='upper center')
    plt.savefig('SOBP')    
"""

make_plots()
print("Image plots saved:"+ image_destination+ ' and '+ image_destination_1)

