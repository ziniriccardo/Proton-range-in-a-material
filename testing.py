# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 17:02:22 2023

@author: ricky
"""

import proton_range as pr

def test_zero_energy():
    particle='proton'
    material='carbon'
    energy=0
    mat_properties=[ 1.7,0.49954, 78e-6, 6]
    stop_powers= pr.compute_range(particle, energy, material, mat_properties)
    #Test if energy=0 corresponds to a zero size vector for stop_powers
    assert len(stop_powers[0])==0
  
    
def test_water_value():
    particle='proton'
    material='water'
    energy=200 
    mat_properties=[ 1.0 ,0.55509, 75e-6, 10]
    stop_powers= pr.compute_range(particle, energy, material, mat_properties)
    final_range= stop_powers[1][stop_powers[4]-1]/mat_properties[0]
    aspected_range= 25.8

    
    min_range=final_range-0.1*aspected_range
    max_range=final_range+ 0.1*aspected_range
    
    #Test if value of range for 200 MeV proton in water is as aspected
    #10% error considered due to secindary fragments and nuclear interaction not considered
    assert final_range>=min_range and final_range<=max_range
    
    
def test_total_energy():
    particle='proton'
    material='carbon'
    energy=70
    mat_properties=[ 1.7,0.49954, 78e-6, 6]
    stop_powers= pr.compute_range(particle, energy, material, mat_properties)
    
    total_energy=0
    de=0
    
    for i in range(0,len(stop_powers[0])-1):
        de=stop_powers[0][i]*(stop_powers[1][i+1]- stop_powers[1][i])
        total_energy+=de
    
    #Test if the sum of all individual de is slower or at most equal to proton energy
    assert total_energy<=energy
  
