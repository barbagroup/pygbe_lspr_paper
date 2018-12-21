'''This file contains functions that help to analyze and plot data related
to the convergence analysis.
'''

import numpy
import pickle
from matplotlib import pyplot, rcParams

def pickleload(pickle_file):
    '''Loads a pickle file and assins it to a variable.
    '''
    with open(pickle_file, 'rb') as f:
        dict_res = pickle.load(f)
    return dict_res

def ord_convergence(array, rate):
    '''Computes the order of convergence given 3 scalar outputs of 3 different
    mesh refinments, saved in an array. The rate is how much the mesh is
    refined. In our case is 4.
    '''

    ord_conv = numpy.log((array[-3] - array[-2])/(array[-2] - array[-1]))/numpy.log(rate)

    return ord_conv


def plot_sph_complex_convergence(N, error, file_name=None, file_ext=None, Ag=None, paper=False):

    if paper:
        file_ext = 'pdf'
        pyplot.switch_backend('agg')
        fig = pyplot.figure(figsize=(3, 2))
        ms = 5
        lw = 1
        fs = 8 
    else:
        pyplot.figure(figsize=(6, 4))
        ms = 10
        lw = 2
        fs = 12

    rcParams['font.family'] = 'serif'
    rcParams['font.size'] = fs
    rcParams['xtick.top'] = True
    rcParams['ytick.right'] = True
    rcParams['axes.linewidth'] = 1

    asymp = N[-3]*error[-3]/N

    if Ag:
        label = 'sphere_Ag'        
    else:
        label = 'BSA_sensor'

    pyplot.loglog(N, error, ls='',marker='o', c='k', mew=1, mfc='w', ms=ms, label=label)
    pyplot.loglog(N, asymp, c='k', marker='None', ls=':', lw=lw, label=None)


    loc = (3*N[-2]+N[-1])/4

    tex_loc = numpy.array((loc,N[-3]*error[-3]/loc))

    
    pyplot.text(tex_loc[0], tex_loc[1],'N$^{-1}$', fontsize=fs,
                rotation=-35,rotation_mode='anchor')
    
    pyplot.xlabel('N')
    pyplot.ylabel('Relative error')
    pyplot.tick_params(axis='both', length=10, width=0.8, which='major', direction='in')
    pyplot.tick_params(axis='both', length=5, width=0.8, which='minor', direction='in')



    pyplot.ylim(1e-3,1)
    pyplot.xlim(1e2,1e5)

    pyplot.legend(loc='upper right', fontsize=fs, numpoints=1, handlelength=0.1).get_frame().set_lw(0.3)
    pyplot.grid(True, which="both")
    
    if (file_name and file_ext):
        fig.savefig('results/'+file_name+'.'+file_ext, format=file_ext, dpi=80, bbox_inches='tight', pad_inches=0.04)

    if paper :
        pyplot.close(fig)
