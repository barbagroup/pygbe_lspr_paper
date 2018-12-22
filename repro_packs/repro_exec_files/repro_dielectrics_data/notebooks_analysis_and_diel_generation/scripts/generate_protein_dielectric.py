import numpy
import sys
from argparse import ArgumentParser


def read_inputs(args):
    """
    Parse command-line arguments to read arguments in main.
    """

    parser = ArgumentParser(description='Read arguments to determine wavelength range')
    parser.add_argument('-s',
                        '--start',
                        type=float,
                        help="Start point for wavelength range")
    parser.add_argument('-e',
                        '--end',
                        type=float,
                        help="End point for wavelength range")
    parser.add_argument('-n',
                        '--points',
                        type=int,
                        help="Number of points in the wavelength range")
    parser.add_argument('-o',
                        '--output',
                        type=str,
                        help="Name of output file")
    
    return parser.parse_args(args)


def protein_dielectric(lamb, Lambda_1, lambda_1, Lambda_array, lambda_array, gamma_array):
    '''Computes the value of dielectric constant of a protein for a certain
       wavelength. It uses Lorentz oscillators, obtained from Pahn, etal. 2013
       
    Arguments:
    ----------
    lamb        : float, wavelength in [nm] where we want to 
                         know the dielectric constant.
    Lambda_1    : float, Lorentz oscillator upper lambda 1. 
    lambda_1    : float, Lorentz oscillator lower lambda 1.
    Lambda_array: array of floats, Lorentz oscillator upper lambda 2,3,4.
    lambda_array: array of floats, Lorentz oscillator lower lambda 2,3,4.
    gamma_array : array of floats, Lorentz oscillator gamma 2,3,4.
    
    Returns:
    --------
    epsilon: complex, dielectric constant.
    '''
    #Let's use the version 1/ thing so it's less confusing
    sigma_1 = 1/Lambda_1
    f_1 = 1/lambda_1
    
    sigma_array = 1/Lambda_array
    alpha_array = 1/gamma_array
    f_array = 1/lambda_array
    
    
    epsilon = 1 + sigma_1**2/(f_1**2 - (1/lamb**2)) + numpy.sum(
                            sigma_array**2/(f_array**2 - 
                                            1j*alpha_array/lamb 
                                          - (1/lamb**2)))
    
    return epsilon

def main(argv=sys.argv):
    '''
    We run protein dielectric for the case of BSA protein.
    
    Arguments passed:
    -----------------
    lamb_start: float, start point for wavelength [nm] range to generate dielectric. 
    lamb_end  : float, end point for wavelength [nm] range to generate dielectric.
    num_points: int, number of points we want in the range.

    Returns:
    --------
    wavelength: array, wavelength array.
    epsilon   : array, dielectric constant array.

    '''

    args = read_inputs(argv[1:])

    lamb_start = args.start
    lamb_end   = args.end
    num_points = args.points
    output_name = args.output


    #define _1 variables
    Lambda_1 = 10853.54
    lambda_1 = 6059.8

    #define the rest (2-4) as an array

    Lambda_array = numpy.array([878.5, 92.6, 82.81])
    gamma_array = numpy.array([2484.52, 155.28, 65.38])
    lambda_array = numpy.array([194.1, 99.38, 57.78])

    #Let's use the version 1/ thing so it's less confusing

    sigma_array = 1/Lambda_array
    alpha_array = 1/gamma_array
    f_array = 1/lambda_array


    wavelength = numpy.linspace(lamb_start,lamb_end,num_points)

    epsilon = numpy.zeros(len(wavelength), dtype=numpy.complex128)

    for i in range(len(wavelength)):
        epsilon[i] = protein_dielectric(wavelength[i], Lambda_1, lambda_1,
                                     Lambda_array, lambda_array, gamma_array)
    
    epsilon_real = epsilon.real
    epsilon_imag = epsilon.imag
    #if desired output of wavelength in Ang, multiply wavelength by 10 in 
    #following line
    numpy.savetxt(output_name, 
                   list(zip(wavelength*10, epsilon_real, epsilon_imag)),
                   fmt='%.1f %.5e %.5e',
                   header='lambda [nm], diel_prot_real, diel_prot_imag')       

    return wavelength, epsilon

if __name__ == "__main__":
    main(sys.argv)