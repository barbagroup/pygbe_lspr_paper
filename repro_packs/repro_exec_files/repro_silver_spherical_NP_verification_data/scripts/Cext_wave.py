"""
To run this case you need to creat the corresponding problem folders with the
appropriate meshes. Here we call them lspr_silver/ and lspr_gold/

"""

import numpy
import time
import sys
import os
from argparse import ArgumentParser

import pygbe
from pygbe.util.read_data import read_fields
from pygbe.main import main

from cext_wavelength_scanning import create_diel_list, Cext_wave_scan, Cext_analytical


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

    argv=sys.argv
    args = read_inputs(argv[1:])

    in_files_path = args.infiles
    #Import silver data
    wave_s, diel_rs, diel_is = numpy.loadtxt('../data/wave_silver_diel_3700-4000.txt', skiprows=1, unpack=True)

    #Import water data
    wave_w, diel_rw, diel_iw = numpy.loadtxt('../data/wave_water_diel_3700-4000.txt', skiprows=1, unpack=True)


    #Creating dielectric list first dielectric outside, then inside
    diel_list = [list(eps) for eps in zip(diel_rw + 1j*diel_iw, diel_rs + 1j*diel_is)]

    #Set enviornment variable for PyGBe
    folder_path = in_files_path + 'BSA_sensorR8_d=infty'
    full_path = os.path.abspath(folder_path)+'/'
    os.environ['PYGBE_PROBLEM_FOLDER'] = full_path

    #Creating dictionary field. We will modify the 'E' key in the for loop.
    field_dict_Ag = read_fields(full_path + 'sph_sensor.config')


    #Calculate Cext(lambda) for silver
    tic_ss = time.time()
    e_field = -0.0037
    wave, Cext_silver = Cext_wave_scan(e_field, wave_s, diel_list, field_dict_Ag, full_path) 
    toc_ss = time.time()



    #Calculate Cext_analytical(lambda) for silver, radius of sphere=8 nm
    tic_sa = time.time()
    r = 8.
    #Silver
    Cext_an_silver = Cext_analytical(r, wave_s/10, diel_rw + 1j*diel_iw, diel_rs + 1j*diel_is)
    toc_sa = time.time()


    #Save wavelength, Cext, Cext_analytical, error
    #Silver
    numpy.savetxt('../results/lambda_Cext_Cext_an_silver.txt', 
                  list(zip(wave/10, Cext_silver, Cext_an_silver)),
                  fmt = '%.5f %.5f %.5f ', 
                  header = 'lambda [ang], Cext, Cext_analytical') 

    time_simulation = (toc_ss - tic_ss) 
    time_analytical = (toc_sa - tic_sa)
    time_silver = (toc_ss - tic_ss) + (toc_sa - tic_sa)


    with open('../results/time_verification.txt', 'w') as f:
        print('time_total: {} s (simulation: {} + analytical: {}) '.format(time_silver, 
               time_simulation, time_analytical), file=f)

if __name__ == "__main__":
    main(sys.argv)
