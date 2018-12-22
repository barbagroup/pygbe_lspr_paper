import numpy
import pygbe 
from pygbe.lspr import main

def create_diel_list(n_out, k_out, n_in, k_in):
    '''Returns the dielectric constant list. Each element contains the
       field('E') for the respective wavelength. i.e each element is a list 
       of the dielectric constant of each region. 
    
    Arguments:
    ----------
    n_out    : array, real part of refractive index in the outside region.
    k_out    : array, imaginary part of refractive index in the outside region.
    n_in     : array, real part of refractive index in the inside region.
    k_in     : array, imaginary part of refractive index in the inside region.

    Returns:
    --------
    diel_out : complex/array of complex, dielectric constant inside surface.
    diel_in  : complex/array of complex, dielectric constant inside surface. 
    diel_list: list, dielectric constant list.
    '''
    
    refrac_out = n_out + 1j * k_out
    refrac_in  = n_in + 1j * k_in

    diel_out = refrac_out * refrac_out 
    diel_in  = refrac_in * refrac_in

    diel_list = [list(eps) for eps in zip(diel_out, diel_in)]
    
    return diel_out, diel_in, diel_list


def Cext_wave_scan(elec_field, wavelength, diel, field_dict, example_folder_path):

    '''Computes the extinction cross section using PyGBe for different 
       wavelength and associated dielectric constants. 

    Arguments:
    ----------
    wavelength         : array/list, wavelengths we want to scan.   
    diel               : list, each element contains the field('E') for the
                         respective wavelength. i.e each element is a list 
                         of the dielectric constant of each region.
    field_dict         : dictionary, config dictionary.
    example_folder_path: str, path to the example folder relative to wherever
                         the interpreter was started. 

    Returns:
    --------  
    Cext_wave          : list, list of cross extinction sections.   
    '''

    Cext_wave = []
    wave_diel = list(zip(wavelength, diel))
    
    for wave, E in wave_diel:
        field_dict['E'] = E  
        results = main(['', example_folder_path], return_results_dict=True,
                       field=field_dict,
                       lspr_values=(elec_field, wave))
        Cext_wave.append(results['Cext_0'])
        

    return wavelength, Cext_wave


def Cext_analytical(radius, wavelength, diel_out, diel_in):
    '''Calculates the analytical solution of the extinction cross section.
       This solution is valid when the nano particle involved is a sphere. 
    
    Arguments:
    ----------
    radius    : float, radius of the sphere in [nm].
    wavelength: float/array of floats, wavelength of the incident
                electric field in [nm].
    diel_out  : complex/array of complex, dielectric constant inside surface.
    diel_in   : complex/array of complex, dielectric constant inside surface. 

    Returns:
    --------
    Cext_an   : float/array of floats, extinction cross section.
      
    '''
    wavenumber = 2*numpy.pi*numpy.sqrt(diel_out)/wavelength
    C1 = wavenumber**2*(diel_in/diel_out-1)/(diel_in/diel_out+2)
    Cext_an = 4*numpy.pi*radius**3/wavenumber.real * C1.imag 
    
    return Cext_an
