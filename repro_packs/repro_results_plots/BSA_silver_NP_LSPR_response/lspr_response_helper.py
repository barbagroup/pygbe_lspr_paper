'''This file contains functions that help to analyze LSPR response to BSA data, 
and to report and plot the main findings.
'''

import numpy
from matplotlib import pyplot, rcParams
import os


def plot_cext_wave_distance(wavelength, cext, linestyles, colors,
                             labels, file_name=None, file_ext=None, paper=False):
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

    if paper:
        file_ext = 'pdf'
        pyplot.switch_backend('agg')
        fig = pyplot.figure(figsize=(3, 2))
        lw = 1
        fs = 8
        fsl = 5
        hl = 0.1
        p = 6
        loc='upper right'
    else:
        fig = pyplot.figure(figsize=(8, 6))
        lw = 2
        fs = 12
        fsl = 12
        hl = 1
        p = 11
        loc='upper right'

    rcParams['font.family'] = 'serif'
    rcParams['font.size'] = fs
    rcParams['xtick.top'] = True
    rcParams['ytick.right'] = True
    rcParams['axes.linewidth'] = 1
    
    ax = fig.add_subplot(1,1,1)

    major_yticks = numpy.linspace(2300, 4300, 5)
    minor_yticks = numpy.linspace(2550, 4050, 4)

    ax.set_yticks(major_yticks)                                                       
    ax.set_yticks(minor_yticks, minor=True)

    #pyplot.yticks(numpy.linspace(2300, 4300, 5))

    pyplot.tick_params(axis='both', length=5, width=0.8,which='major', direction='in')
    pyplot.tick_params(axis='both', length=2.5, width=0.8, which='minor', direction='in')


    pyplot.xlabel('Wavelength [nm]')
    pyplot.ylabel('$C_{ext}$ [$nm^2$]')
    pyplot.xlim(382,387)
    pyplot.ylim(2300, 4300)

    #pyplot.title('LSPR response \n')
    
    for i in range(len(wavelength)):
        pts = p
        pyplot.xticks(numpy.linspace(min(wavelength[i]), max(wavelength[i]), pts),
                     rotation=25)

        pyplot.plot(wavelength[i], cext[i], linestyle=linestyles[i], 
                   color=colors[i], linewidth=lw, label=labels[i])
    
    pyplot.legend(loc=loc, fontsize=fsl, numpoints=2, handlelength=hl).get_frame().set_lw(0.2)
    pyplot.grid(linestyle=':', linewidth=0.5, which='minor')
    pyplot.grid(linestyle=':', linewidth=0.5, which='major')


    if file_name and file_ext:
        pyplot.savefig(file_name+'.'+file_ext, format=file_ext, dpi=80, 
                        bbox_inches='tight', pad_inches=0.04)

    if paper :
        pyplot.close(fig)

def report(sensor_file, bsa_file, file_name=None, file_ext=None, paper=False):
    '''Reports plot of Cext vs wavelength of sensor by itself and when BSA are
       at a distance d of the sensor. 
       It also reports the wavelength at wich the maximum accurs in both cases. 
    '''

    w_d1_00 , Cext_d1_00 = numpy.loadtxt(sensor_file, unpack = True)
    w_d1_2p_00 , Cext_d1_2p_00 = numpy.loadtxt(bsa_file, unpack = True)
    
    wavelength_d1_2p_00 = [w_d1_00/10., w_d1_2p_00/10.]
    cext_d1_00 = [Cext_d1_00, Cext_d1_2p_00]
    linestyles = ['-', ':']
    colors = ['k', '0.6']
    labels = ['$d = \infty$', '$d=1 \,nm$']
    
    plot_cext_wave_distance(wavelength_d1_2p_00, cext_d1_00, linestyles, colors,
                             labels, file_name, file_ext, paper=paper)
    
    if not paper:
        lab = ['d=infty', 'd=1 nm']
        lst = list(zip(cext_d1_00, lab))
        for i in range(len(lst)):
            c, l = lst[i]
            idx = numpy.where(c==max(c))
            print('Cext max at {} is {:.2f} and it occurs at a wavelength of {}'.format(l, 
                    max(c), w_d1_00[idx][0]/10))

def report_2pz(sensor_file, bsa_files_list, file_name=None, file_ext=None, paper=False):
    '''Reports plot of Cext vs wavelength of sensor by itself and when BSA are
       at a distance d of the sensor. For d = 2, 1 and 0.5 nm 
       It also reports the wavelength at which the maximums occur.

       bsa_files_list = list that contains paths of different distances files in
                        descending order.
    '''

    ws , Cext_s = numpy.loadtxt(sensor_file, unpack = True)

    w_d2 , Cext_d2 = numpy.loadtxt(bsa_files_list[0], unpack = True)
    w_d1 , Cext_d1 = numpy.loadtxt(bsa_files_list[1], unpack = True)
    w_d05 , Cext_d05 = numpy.loadtxt(bsa_files_list[2], unpack = True)


    
    wavelength_2p_00 = [ws/10., w_d2/10., w_d1/10., w_d05/10.]
    cext_d1_00 = [Cext_s, Cext_d2, Cext_d1, Cext_d05]
    linestyles = ['-', '--', '-.', ':']
    colors = ['k', '0.2', '0.4', '0.6']
    labels = ['$d = \infty$','$d=2 \,nm$', '$d=1 \,nm$', '$d=0.5 \,nm$']
        
    plot_cext_wave_distance(wavelength_2p_00, cext_d1_00, linestyles, colors,
                             labels, file_name, file_ext, paper=paper)
    
    if not paper:
        lab = ['d=infty', 'd=2 nm', 'd=1 nm', 'd=0.5 nm']
        lst = list(zip(cext_d1_00, lab))
        for i in range(len(lst)):
            c, l = lst[i]
            idx = numpy.where(c==max(c))
            print('Cext max at {} is {:.2f} and it occurs at a wavelength of {}'.format(l, 
                    max(c), ws[idx][0]/10))


def check_file_exists(f_name, f_ext):
    ''' Checks if png image of extinction cross section exists
    '''
    if os.path.exists(f_name+'.'+f_ext):
        file_ext = None
        file_name = None
        print('Plot already exists! If you want to generate it '
            'again, please delete the existing one.')
    else:
        file_ext=f_ext
        file_name = f_name

    return file_ext, file_name