# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 16:53:34 2022

@author: ricky
"""

#Constants


import numpy as np
from math import log as ln


def compute_bethe_bloch(particle,energy,material,mat_properties):
    
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
    
    #vectors for Bethe Bloch
    
    #vectors size
    N=10000
    positions=np.empty(N)
   
    #energy step
    dE=energy/1000
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
        positions[position]=x
        
        #position step
        dx=dE/stop_power
        
        energy_beam=energy_beam-dE
        
        position+=1 
    
        
        
    #re-initialize vectors
    #New loop used to make plots. Needed because stepsize is defined by path length of particle to make each
    #Each point in the plot equally spaced
    x=0
    stop_power=0
    
    #depth step
    dx=positions[position-1]/(1000) 
    
     
    energy_beam=energy
    dE=energy/N
    
    stop_powers_1=np.empty(N)
    positions_1=np.empty(N)
    energies_1=np.empty(N)
    position2=0
    
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
        stop_powers_1[position2]=stop_power
        positions_1[position2]=x
        energies_1[position2]=energy_beam
        
        dE=stop_power*dx
        energy_beam=energy_beam-dE
        
        #define better bragg peak
        
        if (position2>2):
            if  (stop_powers_1[position2]- stop_powers_1[position2-1]> stop_powers_1[position2-1]/15) : break
           
        #print('energies', energies[position2])
        #print('position',positions[position2])
        #print('st.powers',(1/rho)*stop_powers[position2])
    
        position2+=1 
        
    positions_1[position2]=positions[position2-1]
    stop_powers_1[position2]=0
    stop_powers_1[position2-1]=0
    
    #create new arrays 
    plot_stop_powers=np.empty(position2)
    plot_energies=np.empty(position2)
    plot_positions=np.empty(position2)
    
    #fill new arrays
    for i in range(0,position2):
        plot_stop_powers[i]=stop_powers_1[i]
        plot_energies[i]=energies_1[i]
        plot_positions[i]=positions_1[i]
        
    return plot_stop_powers, plot_positions, plot_energies,material, position2
"""
def compute_dose(vector):
    #number of proton per cm**2
    fluence=1e9
    for i in range(0,len(vector[2])):
        
        #factor to convert ev to joule and g to kg (1 Gy=1J/kg)
        conversion=1.6e-12/10**-3
        
        #from energy loss we compute dose in Gy to make its plot-SOBP
        vector[2][i]=conversion*(fluence*vector[2][i])
        return vector 
#compute_bethe_bloch('pion',50,'x')     
"""     
      