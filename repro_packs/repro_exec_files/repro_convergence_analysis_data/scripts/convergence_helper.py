import re
import os
import sys
import time
import numpy
import pickle
import datetime

from pygbe.lspr import main as pygbe

try:
    import pycuda
except ImportError:
    ans = input('PyCUDA not found.  Regression tests will take forever.  Do you want to continue? [y/n] ')
    if ans in ['Y', 'y']:
        pass
    else:
        sys.exit()

mesh = ['512', '2K', '8K', '32K']


def picklesave(test_outputs, file_name):
    with open(file_name,'wb') as f:
        pickle.dump(test_outputs, f, 2)


def mesh_ratio(N):
    """
    Calculates the mesh refinement ratio between consecutive meshes.
    
    Arguments:
    ----------
    N: list, Number of elements / avg_density in test (depends on what applies).

    Returns:
    --------
    mesh_ratio: list of float, mesh refinement ratio between consequtive meshes.         
    """ 
    mesh_ratio = []
    for i in range(len(N)-1):
        mesh_ratio.append(N[i+1]/N[i])

    return mesh_ratio



def run_convergence(mesh, test_name, problem_folder, param):
    """
    Runs convergence tests over a series of mesh sizes

    Inputs:
    ------
        mesh          : array of mesh suffixes
        problem_folder: str, name of folder containing meshes, etc...
        param         : str, name of param file
        
    Returns:
    -------
        N         : len(mesh) array, elements of problem.
        iterations: len(mesh) array, number of iterations to converge.
        Cext_0    : len(mesh) array of float, Cross extinction section of the 
                    main sphere.
        Time      : len(mesh) array of float, time to solution (wall-time)
    """
    print('Runs convergence')
    N = numpy.zeros(len(mesh))
    iterations = numpy.zeros(len(mesh))
    Cext_0 = numpy.zeros(len(mesh))
    Time = numpy.zeros(len(mesh))

    for i in range(len(mesh)):
        try:
            print('Start run for mesh '+mesh[i])
            results = pygbe(['',
                            '-p', problem_folder + '{}'.format(param),
                            '-c', problem_folder +'{}_{}.config'.format(test_name, mesh[i]),
                            '-o', problem_folder + 'output_{}_{}'.format(test_name, mesh[i]),
                            '{}'.format(problem_folder),], return_results_dict=True)

            N[i] = results['total_elements']
            iterations[i] = results['iterations']
            Cext_0[i] = results.get('Cext_0') #We do convergence analysis in the main sphere
            Time[i] = results['total_time']
                 

        except (pycuda._driver.MemoryError, pycuda._driver.LaunchError) as e:
            print('Mesh {} failed due to insufficient memory.'
                  'Skipping this test, but convergence test should still complete'.format(mesh[i]))
            time.sleep(4)
 
    mesh_rate = mesh_ratio(N)
    expected_rate = 0

    if all(ratio==mesh_rate[0] for ratio in mesh_rate):
        expected_rate = mesh_rate[0]
    else:
        print('Mesh ratio inconsistency. \nIf you are running a system protein-sensor, remember \n'
                'that we do not refine the protein mesh, since measurements are taken over the sensor. \n'
                'Do not worry about the warning as soon as the refinement in your sensor mesh keeps a constant \n'
                'ratio. \n'
                'If you are running a case of single sensor, the refinement should keep a constant ratio, \n'
                'otherwise convergence will not be computed properly.')


    return(N, iterations, expected_rate, Cext_0, Time)


def Cext_analytical(radius, wavelength, diel_out, diel_in):
    """
    Calculates the analytical solution of the extinction cross section.
    This solution is valid when the nano particle involved is a sphere. 
    
    Arguments
    ----------
    radius    : float, radius of the sphere in [nm].
    wavelength: float/array of floats, wavelength of the incident
                electric field in [nm].
    diel_out  : complex/array of complex, dielectric constant inside surface.
    diel_in   : complex/array of complex, dielectric constant inside surface. 

    Returns
    --------
    Cext_an   : float/array of floats, extinction cross section.     
    """
    wavenumber = 2 * numpy.pi * numpy.sqrt(diel_out) / wavelength
    C1 = wavenumber**2 * (diel_in / diel_out - 1) / (diel_in / diel_out + 2)
    Cext_an = 4 * numpy.pi * radius**3 / wavenumber.real * C1.imag 
    
    return Cext_an


def richardson_extrapolation_lspr(test_result):
    """
    Performs an estimate of the exact solution using
    Richardson extrapolation, given by

    f_ex = (f_1 * f_3 - f_2^2) / (f_3 - 2*f_2+f_1)

    where f_1 is a result from the finest grid and f_3 is from the coarsest.
    The grids f_1, f_2, f_3 should have the same refinement ratio (e.g. 2 -> 4 -> 8)

    Arguments:
    ----------
    test_result:

    Returns:
    --------
    f_ex : float, richardson_extrapolation estimated exact solution.  
    """
    #We perform the richardson extrapolation in the main body. The body we
    #meassure
    try:
        Cext_0 = test_result['Cext_0']
    except KeyError:
        print('No results found for main body cross extinction section  \n'
              'Something has gone wrong.')
        sys.exit()

    # Using last 3 meshes asumming the latest is the finner one
    f1 = Cext_0[-1] 
    f2 = Cext_0[-2]
    f3 = Cext_0[-3]

    f_ex = (f1 * f3 - f2**2) / (f3 - 2 * f2 + f1)

    return f_ex 

