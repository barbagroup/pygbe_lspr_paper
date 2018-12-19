"""
To run this case you need to creat the corresponding problem folders with the
appropriate meshes. Here we call them BSA_sensor_d=1, BSA_sensor_d=2,
BSA_sensor_d=4 and for the case of no protein BSA_sensor_d=infty. 
"""

import numpy
import time
import os

import pygbe
from pygbe.util.read_data import read_fields
from pygbe.lspr import main

from cext_wavelength_scanning import Cext_wave_scan

#Importing data

#silver
l_w, er_w, ei_w = numpy.loadtxt('../../data/wave_cext_d_prot_sensor/wave_water_diel_ang_3820-3870-5.txt',
                                unpack=True)
l_s, er_s, ei_s = numpy.loadtxt('../../data/wave_cext_d_prot_sensor/wave_silver_diel_ang_3820-3870-5.txt',
                                unpack=True)
l_p, er_p, ei_p = numpy.loadtxt('../../data/wave_cext_d_prot_sensor/wave_prot_diel_ang_3820-3870-5.txt',
                                unpack=True)

'''
l_w, er_w, ei_w = numpy.loadtxt('../../data/wave_cext_d_prot_sensor/wave_water_diel_ang.txt',
                                unpack=True)
l_s, er_s, ei_s = numpy.loadtxt('../../data/wave_cext_d_prot_sensor/wave_silver_diel_ang.txt',
                                unpack=True)
l_p, er_p, ei_p = numpy.loadtxt('../../data/wave_cext_d_prot_sensor/wave_prot_diel_ang.txt',
                                unpack=True)

'''

'''
#gold 
l_w, er_w, ei_w = numpy.loadtxt('../../data/gold_data/wave_water_diel_ang_5170-5270-5.txt',
                                unpack=True)
l_s, er_s, ei_s = numpy.loadtxt('../../data/gold_data/wave_gold_diel_ang_5170-5270-5.txt',
                                unpack=True)
l_p, er_p, ei_p = numpy.loadtxt('../../data/gold_data/wave_prot_diel_ang_5170-5270-5.txt',
                                unpack=True)
'''

#Check the wavelength ranges are all equal
try:
    all(l_w == l_s) & all(l_s == l_p)
    wavelength = l_w
except:
    raise ValueError('The wavelength ranges are not equal, check data generation')
    

#Complex dielectric assembly
e_w = er_w + 1j*ei_w #water
e_s = er_s + 1j*ei_s #silver
e_p = er_p + 1j*ei_p #protein

'''
#Building E field for single sphere dictionary
E_field_single = [list(eps) for eps in zip(e_w, e_s)]

field_dict_single = read_fields('../../../pygbe-master/examples/BSA_sensorR80_d=infty/sph_sensor.config')

tic_single = time.time() 
elec_field =-0.0037
wave_single, Cext_single = Cext_wave_scan(elec_field, wavelength, E_field_single, field_dict_single,
                     '../../../pygbe-master/examples/BSA_sensorR80_d=infty')
toc_single = time.time()

numpy.savetxt('../../data/R8/BSA_sensorR80_d=infty_ef0.0037_370_379.5.txt', 
              list(zip(wave_single, Cext_single)),
              fmt = '%.1f %.8f', 
              header = 'lambda [Ang], Cext, d=infty')

'''

#Building E field for dictionary (protein)
#E_field = [list(eps) for eps in zip(e_w, e_s, e_p)]


e_list = [list(eps) for eps in zip(e_w, e_s, e_p)]

E_field = []
for lst in e_list:
    E_field.append(lst+[lst[-1]]*1)  #works for 2 proteins
#    E_field.append(lst+[lst[-1]]*2)  #works for 3 proteins

#distance_path_folders = ['BSA_sensorR125_d=1', 
#			 'BSA_sensorR125_d=2',
#			 'BSA_sensorR125_d=4']

distance_path_folders = ['BSA_sensorR80_2pz_d=0.1_00']

tic_d = time.time()
elec_field = -0.0037

for path in distance_path_folders:

    folder_path = '../../../pygbe-master/examples/' + path
    full_path = os.path.abspath(folder_path)+'/'
    os.environ['PYGBE_PROBLEM_FOLDER'] = full_path
    
    field_dict = read_fields(folder_path+'/sphere_bsa.config')
    wave, Cext = Cext_wave_scan(elec_field, wavelength, E_field, field_dict,
                     '../../../pygbe-master/examples/'+path)

    numpy.savetxt('../../data/R8/'+path+'.txt', 
              list(zip(wave, Cext)),
              fmt = '%.1f %.8f', 
              header = 'lambda [Ang], Cext'+path)
toc_d = time.time()

with open('../../data/R8/time_wave_Cext_R8_silver_d=0.1nm.txt', 'w') as f:

	print('total run time: {}'.format((toc_d-tic_d)),file=f)
#    print('total run time: {}'.format((toc_single - tic_single)),file=f)
#	print('total run time: {}'.format((toc_single - tic_single)+(toc_d-tic_d)),file=f)
