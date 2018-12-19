import sys
from argparse import ArgumentParser
from convergence_helper import (richardson_extrapolation_lspr, run_convergence, picklesave, mesh)


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


    print('{:-^60}'.format('Running BSA sphere sensor convergence'))

   
    test_outputs = {}

    #This convergence analysis is run for a silver sphere of radius 8nm
    #in a water medium with a BSA protein located at 1 nm of distance over the z-axis
    #The wavelength of the incident electric field is 380 nm 
   

    problem_folder = in_files_path + 'BSA_sensorR8_1pz_d=1_380_convergence/'

    # single sphere lspr
    param = 'sphere_bsa.param'
    test_name = 'sphere_bsa'

    N, iterations, expected_rate, Cext_0, Time = run_convergence(mesh, test_name, problem_folder, param)
    test_outputs[test_name] = {'N': N, 
                                'iterations': iterations,
                                'expected_rate': expected_rate,
                                'Cext_0': Cext_0,
                                'Time': Time} 

    
    Cext_0 = test_outputs[test_name]['Cext_0']

    richardson_ext = richardson_extrapolation_lspr(test_outputs[test_name])


    error = abs(Cext_0 - richardson_ext) / abs(richardson_ext)

    test_outputs[test_name]['error'] = error
    test_outputs[test_name]['rich_extra'] = richardson_ext

    picklesave(test_outputs, '../results/sphere_bsa/'+test_name+'_convergence.pickle')
 

if __name__ == "__main__":
    main(sys.argv)
