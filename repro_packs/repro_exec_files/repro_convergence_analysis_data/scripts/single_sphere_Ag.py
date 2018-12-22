import sys
from argparse import ArgumentParser
from convergence_helper import (Cext_analytical, run_convergence, picklesave, mesh)


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


    print('{:-^60}'.format('Running silver sphere convergence'))

   
    test_outputs = {}

    #This convergence analysis is run for a silver sphere of radius 8nm
    #in a water medium. The wavelength of the incident electric field is 380 nm 
    radius = 8.
    wavelength_Ag = 380.
    diel_out_380 = 1.79721 + 1j * 8.50477e-09 #water value extrapolated
    diel_in_Ag = -3.38765+ 1j * 0.19221 #silver value extrapolated

    analytical_Ag = Cext_analytical(radius, wavelength_Ag, diel_out_380, diel_in_Ag)

    problem_folder = in_files_path + 'sph_sensorR8_convergence/'

    # single sphere lspr
    param = 'sph_sensor_Ag.param'
    test_name = 'sph_sensor_Ag'

    N, iterations, expected_rate, Cext_0, Time = run_convergence(mesh, test_name, problem_folder, param)
    test_outputs[test_name] = {'N': N, 
                                'iterations': iterations,
                                'expected_rate': expected_rate,
                                'Cext_0': Cext_0,
                                'Time': Time} 
    
    Cext_0 = test_outputs[test_name]['Cext_0']

    error = abs(Cext_0 - analytical_Ag) / abs(analytical_Ag)

    test_outputs[test_name]['error'] = error
    test_outputs[test_name]['analytical'] = analytical_Ag

    picklesave(test_outputs, '../results/sph_sensor_Ag/'+test_name+'_convergence.pickle')
 

if __name__ == "__main__":
    main(sys.argv)
