'''This file contains functions that help to analyze and plot data related
to the single silver sphere verification.
'''

import numpy
from matplotlib import pyplot, rcParams


def plot_cext_wave(lamb, cext, cext_an, ylim_s, ylim_e, xpoints, title=None, 
                    file_name=None, file_ext=None, paper=False):

    if paper:
        file_ext = 'pdf'
        pyplot.switch_backend('agg')
        fig = pyplot.figure(figsize=(3, 2))
        ms = 5
        lw = 1
        fs = 8
        hl = 0.2
        fsl = 8
    else:
        pyplot.figure(figsize=(6, 4))
        ms = 7
        lw = 2
        fs = 12
        hl = 1
        fsl = 12

    rcParams['font.family'] = 'serif'
    rcParams['font.size'] = fs
    rcParams['xtick.top'] = True
    rcParams['ytick.right'] = True
    rcParams['axes.linewidth'] = 1
    

    pyplot.plot(lamb, cext, ls='', marker='o', color='0.5', mew=1, mfc='w', ms=ms, label='PyGBe')
    pyplot.plot(lamb, cext_an, ls='--', marker='None',  c='k', lw=lw, label='Analytical')


    pyplot.xlabel('Wavelength [nm]')
    pyplot.ylabel(' $C_{ext}$ [$nm^2$]')
    pyplot.xlim(min(lamb), max(lamb))
    pyplot.ylim(ylim_s, ylim_e)

    pyplot.xticks(numpy.linspace(min(lamb), max(lamb), xpoints), rotation=25)
    pyplot.yticks(numpy.linspace(0, 4000, 9))
    pyplot.tick_params(axis='both', length=5, width=0.8, direction='in')


    
    if title:
        pyplot.title(title)
    
    pyplot.legend(loc='upper right', fontsize=fsl, numpoints=2, handlelength=hl).get_frame().set_lw(0.2)
    pyplot.grid(linestyle=':')

    if file_name and file_ext:
        pyplot.savefig(file_name+'.'+file_ext, format=file_ext, dpi=80, 
                        bbox_inches='tight', pad_inches=0.04)
    if paper :
        pyplot.close(fig)


