# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 17:02:22 2023

@author: ricky
"""

import bragg_peak as bp
import hypothesis

from hypothesis import strategies as st
from hypothesis import settings
from hypothesis import given

#@given(energy=0)
#@settings(max_examples=1)

def test_bethe_bloch():
    particle='proton'
    material='carbon'
    energy=0
    mat_properties=[ 1.7,0.49954, 78e-6, 6]
    stop_powers= bp.compute_bethe_bloch(particle, energy, material, mat_properties)
    assert len(stop_powers[0])==0
  
    
def test_value_bethe_bloch():
    particle='proton'
    material='water'
    energy=200 
    mat_properties=[ 1.0 ,0.55509, 75e-6, 10]
    stop_powers= bp.compute_bethe_bloch(particle, energy, material, mat_properties)
    final_range= stop_powers[1][stop_powers[4]-1]/mat_properties[0]
    aspected_range= 25.8

    
    min_range=final_range-0.1*aspected_range
    max_range=final_range+ 0.1*aspected_range
    
    assert final_range>=min_range and final_range<=max_range
    
    
def test_total_energy():
    particle='proton'
    material='carbon'
    energy=70
    mat_properties=[ 1.7,0.49954, 78e-6, 6]
    stop_powers= bp.compute_bethe_bloch(particle, energy, material, mat_properties)
    
    total_e=0
    de=0
    
    for i in range(0,len(stop_powers[0])-1):
        de=stop_powers[0][i]*(stop_powers[1][i+1]- stop_powers[1][i])
        total_e+=de
    
    assert total_e<=energy
