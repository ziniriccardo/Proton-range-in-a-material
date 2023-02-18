# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 16:53:34 2022

@author: ricky
"""

import numpy as np
from math import log as ln


def compute_range(particle,energy,material,mat_properties):
    
    """"
    This method performs a range calculation for a proton in a chosen material
    
    Parameters
        particle: incoming particle, proton
        energy: energy of the incoming particle
        material: target material 
        mat_properties: properties of the material: density (rho), ratio Z/A (Z_over_A), ionization energy (e_ioniz) and number of protons Z.
        
    """
    
    #Contants for Bethe Bloch calculation
  
    # Mev*cm^2/g
    K=0.307075 
    #electron mass  MeV/c**2
    m_e=0.510998918    
   
    #range in g/cm**2
    x=0
    dx=0
    stop_power=0
    energy_beam=energy
    part_mass= 938.272
    #proton charge
    z=1
    part_rest_energy=part_mass
    
    #vectors size
    N=10000
    
    positions=np.empty(N)
    #energy step
    dE=energy/1000
    #position index
    i=0
            
    while energy_beam>0 and stop_power>=0:

        x=x+ dx    
        
        gamma= energy_beam/part_rest_energy +1 
        beta=np.sqrt(1-(1/gamma**2))
        
        beta_gamma=beta*gamma
    
        tmax= (2*m_e*(gamma*beta)**2)/(1+ (2*gamma*m_e)/part_mass+(m_e/part_mass)**2)

        energy_plasma=28.816e-6*np.sqrt(mat_properties[0]*mat_properties[1])
        
        #corrections 
        delta_corr=ln(energy_plasma*beta_gamma/mat_properties[2])+1
        shell=-(2*ln(mat_properties[2]/energy_plasma)+1)
                
        stop_power=(K*z**2*mat_properties[1]/beta**2)*(0.5*ln( 2*m_e*beta_gamma**2*tmax/mat_properties[2]**2)- beta**2 -delta_corr/2 -shell/mat_properties[3] )       
        
        #position step
        dx=dE/stop_power
        
        energy_beam=energy_beam-dE
        positions[i]=x     
       
        i+=1 
            
    #re-initialize vectors
    #New loop used to make plots. Needed because stepsize is defined by path length of particle to make each
    #Each point in the plot equally spaced
    
    x=0
    stop_power=0
    
    #depth step
    dx=positions[i-1]/(1000) 
    
    energy_beam=energy
    
    #create arrays
    stop_powers=np.empty(i)
    positions=np.empty(i)
    energies=np.empty(i)
    
    #position index
    position=0
    
    while energy_beam>0 and stop_power>=0:
        x=x+ dx    
        
        gamma= energy_beam/part_rest_energy +1 
        beta=np.sqrt(1-(1/gamma**2))
        
        beta_gamma=beta*gamma
    
        tmax= (2*m_e*(gamma*beta)**2)/(1+ (2*gamma*m_e)/part_mass+(m_e/part_mass)**2)

        energy_plasma=28.816e-6*np.sqrt(mat_properties[0]*mat_properties[1])
        
        #corrections
        delta_corr=ln(energy_plasma*beta_gamma/mat_properties[2])+1
        shell=-(2*ln(mat_properties[2]/energy_plasma)+1)
                 
        stop_power=(K*z**2*mat_properties[1]/beta**2)*(0.5*ln( 2*m_e*beta_gamma**2*tmax/mat_properties[2]**2)- beta**2 -delta_corr/2 -shell/mat_properties[3] ) 
        
        #Fill arrays
        stop_powers[position]=stop_power
        positions[position]=x
        energies[position]=energy_beam
        
        dE=stop_power*dx
        energy_beam=energy_beam-dE
       
        #Define better the Bragg Peak
        
        if (position>2):
            if  (stop_powers[position]- stop_powers[position-1]> stop_powers[position-1]/15) : break
                
        position+=1 
    
    if position!=0:
        positions[position]=positions[position-1]
        stop_powers[position]=0
        stop_powers[position-1]=0
        
    #create plot arrays 
    plot_stop_powers=np.empty(position)
    plot_energies=np.empty(position)
    plot_positions=np.empty(position)
    
    #fill plot arrays
    for i in range(0,position):
        
        plot_stop_powers[i]=stop_powers[i]
        plot_energies[i]=energies[i]
        plot_positions[i]=positions[i]
    
    return plot_stop_powers, plot_positions, plot_energies, material, position      
