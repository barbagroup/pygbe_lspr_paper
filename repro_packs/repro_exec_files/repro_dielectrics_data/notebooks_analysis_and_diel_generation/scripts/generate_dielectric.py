import numpy
import sys
from data_analysis_helper import linear_interp
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

    parser.add_argument('-d',
                        '--data',
                        type=str,
                        help="Path of data we want to interpolate to get diel")

    parser.add_argument('-o',
                        '--output',
                        type=str,
                        help="Name of output file")
    
    return parser.parse_args(args)


def main(argv=sys.argv):
    '''
    Get dielectric constant as a function of wavelength by interpolating
    extisting data in terms of refraction index.

    Arguments passed (read docs of read_inputs):
    -----------------
    lamb_start: float, start point for wavelength range to generate dielectric. 
    lamb_end  : float, end point for wavelength range to generate dielectric.
    num_points: int, number of points we want in the range.
    data_interpolate: str, path of data we want to interpolate to get 
                        dielectric constant.
    Returns:
    --------
    wavelength: array, wavelength array.
    epsilon   : array, dielectric constant array.

    '''

    args = read_inputs(argv[1:])

    lamb_start  = args.start
    lamb_end    = args.end
    num_points  = args.points
    data_path   = args.data
    output_name = args.output

    wavelength = numpy.linspace(lamb_start, lamb_end, num_points)

    lambda_m, n_m, k_m = numpy.loadtxt(data_path, unpack = True)
    
    n_interp, k_interp = linear_interp(lambda_m, n_m, k_m)

    n_range = n_interp(wavelength)
    k_range = k_interp(wavelength)

    diel = (n_range + 1j*k_range)**2

    diel_real = diel.real 
    diel_imag = diel.imag 

    numpy.savetxt(output_name, 
                   list(zip(wavelength, diel_real, diel_imag)),
                   fmt='%.1f %.5e %.5e',
                   header='lambda [ang], diel_real, diel_imag')       

    return wavelength, diel 

if __name__ == "__main__":
    main(sys.argv)