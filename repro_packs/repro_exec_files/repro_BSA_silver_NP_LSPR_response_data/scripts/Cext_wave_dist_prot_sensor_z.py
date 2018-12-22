import numpy
import time
import sys
import os
from argparse import ArgumentParser

import pygbe
from pygbe.util.read_data import read_fields
from pygbe.lspr import main

from cext_wavelength_scanning import Cext_wave_scan


def read_inputs(args):
    """
    Parse command-line arguments to read arguments in main.
    """

    parser = ArgumentParser(description='Read path where input files are located')
    parser.add_argument('-if',
                        '--infiles',
                        type=str,
                        help="Absolute path where input files are located (downloaded from zenodo)")
    
    return parser.parse_args(args)




def main(argv=sys.argv):
    '''Creates lspr response data for the following cases:
    BSA_sensorR8_2pz_d=0.5_00, BSA_sensorR8_2pz_d=1_00, BSA_sensorR8_2pz_d=2_00 
    and for the case of no protein BSA_sensorR8_d=infty. 

    Arguments passed (read docs of read_inputs)
    ----------------
    infiles: str, absolute path where the input files are located. 

    For example: if input_problem_folders was downloaded in the directory 
    home/Downloads, then the path will be:

    home/Downloads/input_problem_folders/
    '''

    argv=sys.argv
    args = read_inputs(argv[1:])

    in_files_path = args.infiles


    #Importing dielectrics data

    l_w, er_w, ei_w = numpy.loadtxt('../dielectrics_data/wave_ang_water_diel_3820-3870.txt',
                                    unpack=True)
    l_s, er_s, ei_s = numpy.loadtxt('../dielectrics_data/wave_ang_silver_diel_3820-3870.txt',
                                    unpack=True)
    l_p, er_p, ei_p = numpy.loadtxt('../dielectrics_data/wave_ang_prot_diel_3820-3870.txt',
                                    unpack=True)


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


    #Building E field for single sphere dictionary
    E_field_single = [list(eps) for eps in zip(e_w, e_s)]

    field_dict_single = read_fields(in_files_path +'BSA_sensorR8_d=infty/sph_sensor.config')

    tic_single = time.time() 
    elec_field =-0.0037
    wave_single, Cext_single = Cext_wave_scan(elec_field, wavelength, E_field_single, field_dict_single,
                         in_files_path +'BSA_sensorR8_d=infty/')
    toc_single = time.time()

    numpy.savetxt('../Cext_variation_with_distance_two_bsa_z_results/BSA_sensorR8_d=infty_3820-3870ang.txt', 
                  list(zip(wave_single, Cext_single)),
                  fmt = '%.1f %.8f', 
                  header = 'lambda [Ang],Cext_'+'BSA_sensorR8_d=infty')



    #Building E field for dictionary (one protein) uncomment the following line
    #E_field = [list(eps) for eps in zip(e_w, e_s, e_p)

    #If only one protein comment the following 4 lines of code

    #Building E field for dictionary for case of 2 proteins
    e_list = [list(eps) for eps in zip(e_w, e_s, e_p)]

    E_field = []
    for lst in e_list:
        E_field.append(lst+[lst[-1]]*1)  #works for 2 proteins, if n proteins
                                         # needed replace lst+[lst[-1]]*1 by
                                         #lst+[lst[-1]]*(n-1)


    distance_path_folders = ['BSA_sensorR8_2pz_d=0.5_00', 
    			             'BSA_sensorR8_2pz_d=1_00',
    			             'BSA_sensorR8_2pz_d=2_00']



    tic_d = time.time()
    elec_field = -0.0037

    for path in distance_path_folders:

        folder_path = in_files_path + path
        full_path = os.path.abspath(folder_path)+'/'
        os.environ['PYGBE_PROBLEM_FOLDER'] = full_path
        
        field_dict = read_fields(folder_path+'/sphere_bsa.config')
        wave, Cext = Cext_wave_scan(elec_field, wavelength, E_field, field_dict,
                         in_files_path + path)

        numpy.savetxt('../Cext_variation_with_distance_two_bsa_z_results/'+path+'_3820-3870ang.txt', 
                  list(zip(wave, Cext)),
                  fmt = '%.1f %.8f', 
                  header = 'lambda [Ang], Cext_'+path)
    toc_d = time.time()

    with open('../Cext_variation_with_distance_two_bsa_z_results/Time_Cext_variation_with_distance_two_bsa_z.txt', 'w') as f:
        print('single sphere run time: {}'.format((toc_single - tic_single)),file=f)
        print('sphere-bsa run time: {}'.format((toc_d-tic_d)),file=f)
        print('total run time: {}'.format((toc_single - tic_single)+(toc_d-tic_d)),file=f)


if __name__ == "__main__":
    main(sys.argv)
