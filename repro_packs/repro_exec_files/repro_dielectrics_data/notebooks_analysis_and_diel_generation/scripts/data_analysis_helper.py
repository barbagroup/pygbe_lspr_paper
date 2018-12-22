import numpy 
from matplotlib import pyplot, rcParams
from scipy.interpolate import interp1d, splev, splrep

def wave_filter_interp(lambda_eval, lambda_interp):
    '''It removes the data points of a wavelength array, that are out of the
       range where the resulting interpolation is valid.  

    Arguments:
    ----------
    lambda_eval    : array, wavelength array that where we want to evaluate the
                     resulting function of 
    lambda_interp  : array, wavelength array of the interpolated data. 

    Returns:
    --------
    lambda_eval_new: array, wavelength array ready for evaluation. 
    idx_min        : int, index where the slicing of lambda_eval starts. 
    idx_max        : int, index where the slicing of lambda_eval ends.

    '''

    lam_min = numpy.where(lambda_eval<min(lambda_interp))[0]

    if len(lam_min)>0:
        idx_min = max(lam_min) + 1
    else:
        idx_min = 0

    lam_max = numpy.where(lambda_eval>max(lambda_interp))[0]

    if len(lam_max)>0:
        idx_max = min(lam_max)
    else:
        idx_max = None

    lambda_eval_new = lambda_eval[idx_min:idx_max]

    return lambda_eval_new, idx_min, idx_max


def nm_from_ev(electron_volts):
    '''Returns wavelength in nanometers [nm] from energy given in electron
       volts [eV].

    Arguments:
    ----------
    electron_volts: float/array, energy in electron volts [eV]

    Returns:
    --------
    lamb_nm = float/array, wavelength in nanometers [nm]
    '''

    h = 4.13566766225e-15 # Planck's contant in [eV.s]
    c = 2.99792458e17 # light velocity in [nm/s]
    
    lamb_nm = h*c / electron_volts 

    return lamb_nm

def linear_interp(lamb, n, k):
    '''Returns the linear interpolation of the real and imaginary refractive index.
    
    Arguments:
    ----------
    lamb: array, wavelengths.
    n   : array, real part of refractive index. 
    k   : array, imaginary part of refractive index.
    
    Returns:
    --------
    real_inter: function, interpolated function of the real part of the refrac index.
    imag_inter: function, interpolated function of the imaginary part the refrac index.
    
    '''
    real_inter = interp1d(lamb, n)
    imag_inter = interp1d(lamb, k)
    
    return real_inter, imag_inter


def spline(lamb, n, k):
    '''Returns the B-spline representations of the real and imaginary refractive index.
    
    Arguments:
    ----------
    lamb: array, wavelengths.
    n   : array, real part of refractive index. 
    k   : array, imaginary part of refractive index.
    
    Returns:
    --------
    real_tuple: tuple, vector of knots, spline coefficients, and the degree of the spline
                of the real part of the refrac index.
    imag_tuple: tuple, vector of knots, spline coefficients, and the degree of the spline
                of the imaginary part of the refrac index.
    '''
    
    real_tuple = splrep(lamb, n)
    imag_tuple = splrep(lamb, k)
    
    return real_tuple, imag_tuple


def spline_eval(x, real_tuple, imag_tuple): 
    '''Evaluates the B-splines of the real and imaginary refractive index.
    
    Arguments:
    ----------
    x         : array,  points at which to return the value of the spline.
    real_tuple: tuple, vector of knots, spline coefficients, and the degree of the spline
                of the real part of the refrac index.
    imag_tuple: tuple, vector of knots, spline coefficients, and the degree of the spline
                of the imaginary part of the refrac index.
    
    
    Returns:
    --------    
    real_spline: array, values representing the spline function evaluated at the points in
                 x for real refractive index.
    imag_spline: array, values representing the spline function evaluated at the points in
                 x for real refractive index.    
    '''
    
    real_spline = splev(x, real_tuple)
    imag_spline = splev(x, imag_tuple)
    
    return real_spline, imag_spline

def plot_refrac(lamb, n, k):    
    """
    Plots the refractive index vs wavelength.
    Plots separately the real and imaginary part of the refractive index.
    
    Arguments:
    ----------
    lamb: array, wavelengths.
    n   : array, real part of refractive index. 
    k   : array, imaginary part of refractive index.
    
    Returns:
    --------
    Plots of refrac_index_real vs lambda, refrac_index_imaginary vs lambda. 
    """
    
    pyplot.figure(figsize=(12,4))  

    pyplot.subplot(121)
    
    pyplot.scatter(lamb,n, color='#2929a3') 
    
    pyplot.xlabel('Wavelength [nm]')
    pyplot.ylabel('Refractive index')
    pyplot.xlim(min(lamb)-5, max(lamb)+5)
    pyplot.xticks(numpy.linspace(min(lamb), max(lamb), 10), rotation=25)
    pyplot.title('Real')
    pyplot.grid(linestyle=':')
    
    
    pyplot.subplot(122)
    
    pyplot.scatter(lamb,k, color='#ff5733') 
    
    pyplot.xlabel('Wavelength [nm]')
    #pyplot.ylabel('Refractive index')
    pyplot.xlim(min(lamb)-5, max(lamb)+5)
    pyplot.xticks(numpy.linspace(min(lamb), max(lamb), 10), rotation=25)
    pyplot.title('Imaginary')
    pyplot.grid(linestyle=':')

def plot_interpolation(lamb, n, k, lamb_x, real_linear, imag_linear, real_spline, imag_spline):
    '''Plots data, linear interpolation and spline of the real and imaginary refractive index
    
    Arguments:
    ----------    
    lamb       : array, wavelengths.
    n          : array, real part of refractive index. 
    k          : array, imaginary part of refractive index.
    lamb_x     : array,  points at which to return the value of the spline
    real_linear: function, interpolated function of the real part of the refrac index.
    imag_linear: function, interpolated function of the imaginary part the refrac index.
    real_spline: array, values representing the spline function evaluated at the points in
                 x for real refractive index.
    imag_spline: array, values representing the spline function evaluated at the points in
                 x for real refractive index.        
    '''
    
    pyplot.figure(figsize=(12,12))  

    #Real refrac index
    pyplot.subplot(211)
    #data
    pyplot.scatter(lamb, n, color='#2929a3', alpha = 0.8, label = 'data')
    #linear interp
    pyplot.plot(lamb_x, real_linear(lamb_x), color = 'r', ls = '-', label = 'linear')
    #spline interp
    pyplot.plot(lamb_x, real_spline, color = 'g', ls = '--', label = 'spline')
    
    pyplot.xlim(min(lamb)-5, max(lamb)+5)
    pyplot.xticks(numpy.linspace(min(lamb), max(lamb), 20), rotation=25)
    pyplot.title('Real')
    pyplot.ylabel('Refractive index')
    pyplot.legend(loc='best')
    pyplot.grid(linestyle=':')
    
    #Imaginary refrac index
    pyplot.subplot(212)
    #data
    pyplot.scatter(lamb, k, color='#2929a3', alpha = 0.8, label = 'data') 
    #linear interp
    pyplot.plot(lamb_x, imag_linear(lamb_x), color = 'r', ls = '-', label = 'linear')
    #spline interp
    pyplot.plot(lamb_x, imag_spline, color = 'g', ls = '--', label = 'spline')
    
    pyplot.xlim(min(lamb)-5, max(lamb)+5)
    pyplot.xticks(numpy.linspace(min(lamb), max(lamb), 20), rotation=25)
    pyplot.title('Imaginary')
    pyplot.ylabel('Refractive index')
    pyplot.xlabel('Wavelength [nm]')
    pyplot.legend(loc='best')
    pyplot.grid(linestyle=':')

def plot_sph_complex_convergence(N_Ag, N_Au, error_Ag, error_Au):
    """
    Plots grid convergence for silver and gold sphere lspr problems.

    Arguments:
    ----------
    N    : list, number of elements of meshes picked for convergence analysis. 
    error: list, relative error compared to the analytical solution.
    """
    pyplot.figure(figsize=(8,5))

    rcParams['font.family'] = 'serif'
    rcParams['font.size'] = 16
    rcParams['xtick.top'] = True
    rcParams['ytick.right'] = True
    rcParams['axes.linewidth'] = 2

    asymp_Ag = N_Ag[-2]*error_Ag[-2]/N_Ag
    asymp_Au = N_Au[-2]*error_Au[-2]/N_Au


    pyplot.loglog(N_Ag, error_Ag, ls='',marker='o', c='k', mew=1.5, mfc='w', ms=10, label='Ag')
    pyplot.loglog(N_Ag, asymp_Ag, c='k', marker='None', ls=':', lw=2, label=None)

    pyplot.loglog(N_Au, error_Au, ls='',marker='s', c='k', mew=1.5, mfc='w', ms=10, label='Au')
    pyplot.loglog(N_Au, asymp_Au, c='k', marker='None', ls=':', lw=2, label=None)

    loc_Ag = (3*N_Ag[-2]+N_Ag[-1])/4
    loc_Au = (3*N_Au[-2]+N_Au[-1])/4

    tex_loc_Ag = numpy.array((loc_Ag,N_Ag[-1]*error_Ag[-1]/loc_Ag))
    tex_loc_Au = numpy.array((loc_Au,N_Au[-1]*error_Au[-1]/loc_Au))

    pyplot.text(tex_loc_Ag[0], tex_loc_Ag[1],'N$^{-1}$', fontsize=12,
                rotation=-35,rotation_mode='anchor')
    pyplot.text(tex_loc_Au[0], tex_loc_Au[1],'N$^{-1}$',fontsize=12,
                rotation=-35,rotation_mode='anchor')

    pyplot.xlabel('N')
    pyplot.ylabel('Relative error')
    pyplot.tick_params(axis='both', length=10, width=1, which='major', direction='in')
    pyplot.tick_params(axis='both', length=5, width=1, which='minor', direction='in')
    pyplot.ylim(1e-4,1)
    pyplot.xlim(1e2,1e5)
    pyplot.legend(loc='best')
    pyplot.grid(True, which="both")

    #Uncomment if desired to save figure
    #pyplot.savefig('figures/Cext_convergence_sph_Ag_Au.pdf', dpi=80, format='pdf')

def plot_cext_wave(lamb, cext, cext_an, ylim_s, ylim_e, xpoints, title=None):
    rcParams['font.family'] = 'serif'
    rcParams['font.size'] = 14
    rcParams['xtick.top'] = True
    rcParams['ytick.right'] = True
    rcParams['axes.linewidth'] = 2
    
    pyplot.figure(figsize=(9,6))

    pyplot.plot(lamb, cext, ls='', marker='o', color='0.4', mew=1.5, mfc='w', ms=7, label='PyGBe')
    pyplot.plot(lamb, cext_an, ls='--', marker='None',  c='k', lw=1.5, label='Analytical')


    pyplot.xlabel('Wavelength [nm]')
    pyplot.ylabel('Cross extinction section [$nm^2$]')
    pyplot.xlim(min(lamb), max(lamb))
    pyplot.ylim(ylim_s, ylim_e)

    pyplot.xticks(numpy.linspace(min(lamb), max(lamb), xpoints), rotation=25)
    pyplot.tick_params(axis='both', length=8, width=1, direction='in')
    pyplot.title(title)
    pyplot.legend(loc='best')
    pyplot.grid(linestyle=':')

    #Uncomment if desired to save figure
    #pyplot.savefig('figures/cext_wave_'+title+'.pdf', dpi=80, format='pdf');

def plot_sph_multiple_complex_convergence(avg_density, error):
    """
    Plots grid convergence for multiple spheres lspr problem.

    Arguments:
    ----------
    avg_density: list, avg elements/nm^2  of meshes picked for convergence analysis. 
    error      : list, relative error compared to the analytical solution.
    """

    rcParams['font.family'] = 'serif'
    rcParams['font.size'] = 16
    rcParams['xtick.top'] = True
    rcParams['ytick.right'] = True
    rcParams['axes.linewidth'] = 2

    asymp = avg_density[-2]*error[-2]/avg_density

    pyplot.figure(figsize=(8,5))

    pyplot.loglog(avg_density, error, ls='',marker='o', c='k', mew=1.5, mfc='w', ms=10)
    pyplot.loglog(avg_density, asymp, c='k', marker='None', ls=':', lw=2)

    
    loc = (3*avg_density[-2]+avg_density[-1])/4

    tex_loc = numpy.array((loc,avg_density[-1]*error[-1]/loc))

    pyplot.text(tex_loc[0], tex_loc[1],'avg_den$^{-1}$', fontsize=12,
                rotation=-35,rotation_mode='anchor')
    

    pyplot.xlabel('Average elements/$nm^2$')
    pyplot.ylabel('Relative error')
    pyplot.tick_params(axis='both', length=10, width=1, which='major', direction='in')
    pyplot.tick_params(axis='both', length=5, width=1, which='minor', direction='in')
    pyplot.ylim(1e-3,1)
    pyplot.xlim(1e-1,1e2)
    pyplot.grid(True, which="both")

    #Uncomment if desired to save figure
    #pyplot.savefig('figures/Cext_convergence_mult_sph.pdf', dpi=80, format='pdf')
    
def plot_cext_wave_distance(wavelength, cext, linestyles, colors, labels):
    '''Plots the cross extinction section as a function of wavelength for
    different values of distance at which the proteins are located.

  	Arguments:
    ----------
    wavelength: list of wavelength arrays for each distance case.
    cext      : list of cross extinction section arrays for each distance case.
    linestyles: list of linstyles we desire to use for each distance case.
    colors    : list of colors we desire to use for each distance case.
    labels    : list of labels we desire to use for each distance case.
	'''
    rcParams['font.family'] = 'serif'
    rcParams['font.size'] = 16
    rcParams['xtick.top'] = True
    rcParams['ytick.right'] = True
    rcParams['axes.linewidth'] = 2

    fig=pyplot.figure(figsize=(9,6))
    ax = fig.add_subplot(1,1,1)
    
    major_xticks = numpy.linspace(min(wavelength[0]), max(wavelength[0]), 11)
    minor_xticks = numpy.linspace(min(wavelength[0]), max(wavelength[0]), 41)
    major_yticks = numpy.linspace(0, 8000, 9)
    minor_yticks = numpy.linspace(0, 8000, 33)

    ax.set_xticks(major_xticks)                                                       
    ax.set_xticks(minor_xticks, minor=True)
    ax.set_yticks(major_yticks)                                                       
    ax.set_yticks(minor_yticks, minor=True)

    pyplot.xticks(rotation=25)
    pyplot.tick_params(axis='both', length=5, width=1, which='major', direction='in')
    pyplot.tick_params(axis='both', length=2.5, width=1, which='minor', direction='in')

    pyplot.xlabel('Wavelength [nm]')
    pyplot.ylabel('Cross extinction section [$nm^2$]')
    pyplot.xlim(380,400)
    pyplot.ylim(0,8000)
    pyplot.grid(ls=':', which='minor', alpha=0.4)
    pyplot.grid(ls=':', which='major', alpha=0.8)
    #pyplot.title('Silver sphere with BSA Proteins')
    
    for i in range(len(wavelength)):
        pyplot.plot(wavelength[i], cext[i], linestyle=linestyles[i], 
                   color=colors[i], linewidth=2, label=labels[i])
    
    pyplot.legend(loc='best')

    #Uncomment if desired to save figure
    #pyplot.savefig('figures/Cext_wave_distance.pdf', dpi=80, format='pdf')

