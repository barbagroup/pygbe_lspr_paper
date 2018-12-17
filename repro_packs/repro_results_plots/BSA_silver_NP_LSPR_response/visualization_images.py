'''This file contains functions that help to produce the images of the proteins
locations respect to the sensor. 
'''

import numpy
from matplotlib import pyplot, rcParams
from mpl_toolkits.mplot3d import Axes3D
import os


def read_data_plot(sensor, prt_one, prt_two, elev, azim, prot_color,
                    file_name=None, file_ext=None, fig_size=None):
    '''Reads the mesh files (.vert and .face) necessary to plot the 
    sensor-proteins display and save them as png. 

    Arguments:
    ---------
    sensor : str, path to the sensor mesh files without the extention. 
    prt_one: str, path to the protein one mesh files without the extention. 
    prt_two: str, path to the protein two files without the extention.

    Example:
    If the location of the mesh files, sensor.vert and sensor.face, is mesh_files/
    then:
    sensor = 'mesh_files/sensor' 

    elev  : float, set the elevation of the axes (elevation angle in the z plane). 
    azim  : float, set the azimuth of the axes (azimuth angle in the x,y plane).    
    '''

    #load sensor
    xs, ys, zs = numpy.loadtxt(fname=sensor+'.vert', unpack=True)
    face_s = numpy.loadtxt(fname=sensor+'.face') 
    face_sensor = face_s[:][:] - 1

    #load protein 1
    xp1, yp1, zp1 = numpy.loadtxt(fname=prt_one+'.vert', unpack=True) 
    f_11, f_21, f_31, g1, h1 = numpy.loadtxt(fname=prt_one+'.face', unpack=True)

    face_prt1 = numpy.array(list(zip(f_11, f_21, f_31)))
    face_protein_1 = face_prt1[:][:] - 1

    #load protein 2
    xp2, yp2, zp2 = numpy.loadtxt(fname=prt_two+'.vert', unpack=True)  
    f_12, f_22, f_32, g2, h2 = numpy.loadtxt(fname=prt_two+'.face', unpack=True)

    face_prt2 = numpy.array(list(zip(f_12, f_22, f_32)))
    face_protein_2 = face_prt2[:][:] - 1

    ### Plot image ###

    pyplot.switch_backend('agg')         # We changed the backend to not generate the interactive image  
    
    fig = pyplot.figure(figsize=fig_size)
    #fig.set_figheight(fig_size[1])
    #fig.set_figwidth(fig_size[0])

    ax = fig.gca(projection='3d')


    ax.plot_trisurf(xs, ys, zs, triangles=face_sensor, linewidth=0.1,
                     edgecolor="black", color="white", alpha=0.2)
    ax.plot_trisurf(xp1, yp1, zp1, triangles=face_protein_1, linewidth=0.1,
                     edgecolor=prot_color, color="white", alpha=0.1 )
    ax.plot_trisurf(xp2, yp2, zp2, triangles=face_protein_2, linewidth=0.1,
                     edgecolor=prot_color, color="white", alpha=0.1 )

    ax.set_xlabel('X [$\AA$]')
    ax.set_ylabel('Y [$\AA$]')
    ax.set_zlabel('Z [$\AA$]')

    ax.xaxis.labelpad = 8
    ax.yaxis.labelpad = 8
    ax.zaxis.labelpad = 8

    arrayOfTicks = numpy.linspace(-200, 200, 11)

    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False

    #ax.xaxis._axinfo["grid"].update({"linewidth":0.1, "color" : '0.7'})
    #ax.yaxis._axinfo["grid"].update({"linewidth":0.1, "color" : '0.7'})
    #x.zaxis._axinfo["grid"].update({"linewidth":0.1, "color" : '0.7'})
    
    ax.grid(True)
    
    ax.w_xaxis.set_ticks(arrayOfTicks) 
    ax.w_yaxis.set_ticks(arrayOfTicks) 
    ax.w_zaxis.set_ticks(arrayOfTicks) 

    ilim = arrayOfTicks.min()
    slim = arrayOfTicks.max()

    ax.set_xlim3d(ilim, slim)
    ax.set_ylim3d(ilim, slim)
    ax.set_zlim3d(ilim, slim)

    ax.tick_params(pad=6)
    pyplot.xticks(rotation=30)
    pyplot.yticks(rotation=30)

    #pyplot.tight_layout()

    if (azim==-90):
        ax.w_yaxis.set_ticklabels([])
        ax.set_ylabel('')

    if (azim==-180):
        ax.w_xaxis.set_ticklabels([])
        ax.set_xlabel('')


    ax.view_init(elev, azim)

    if (file_name and file_ext):
        fig.savefig('figures/'+file_name+'.'+file_ext, bbox_inches='tight',
                    format=file_ext, pad_inches=-0.75)

def file_exist(files_list):
    '''Checks if images files exist
    '''
    status = list()
    for file in files_list:
        if os.path.exists('figures/'+file):
            status.append(True)
        else:
            status.append(False)

    status = all(status)

    return status

def main(paper=False):
    ''' Generates all the png for sphere-BSA visualizations.
    '''

    if paper:
        file_ext = 'pdf'
        fig_size = (9, 9)
        fs = 10
    else:
        file_ext = 'png'
        fig_size = (9, 9)
        fs = 10


    rcParams['font.family'] = 'serif'
    rcParams['font.size'] = fs
    

    #Case of 2 proteins in z
    sensor = 'mesh_files/sensor/sensor_2K_R8nm'
    prt_1z = 'mesh_files/BSA_sensor_2pz_d=1_00/bsa_d0.3_R8+1nm_z'
    prt_2z = 'mesh_files/BSA_sensor_2pz_d=1_00/bsa_d0.3_R8+1nm_-z'


    read_data_plot(sensor, prt_1z, prt_2z, elev=0, azim=-90,
                                        prot_color='red',
                                        file_name='2prot_1nm_z_R8nm',
                                        file_ext=file_ext,
                                        fig_size=fig_size)
    
    #Case of 2 proteins in x
    prt_1x = 'mesh_files/BSA_sensor_2px_d=1_00/bsa_d0.3_R8+1nm_x'
    prt_2x = 'mesh_files/BSA_sensor_2px_d=1_00/bsa_d0.3_R8+1nm_-x'


    read_data_plot(sensor, prt_1x, prt_2x, elev=0, azim=-90,
                                        prot_color='blue',
                                        file_name='2prot_1nm_x_R8nm',
                                        file_ext=file_ext,
                                        fig_size=fig_size)
    #Case of 2 proteins in y
    prt_1y = 'mesh_files/BSA_sensor_2py_d=1_00/bsa_d0.3_R8+1nm_y'
    prt_2y = 'mesh_files/BSA_sensor_2py_d=1_00/bsa_d0.3_R8+1nm_-y'


    read_data_plot(sensor, prt_1y, prt_2y, elev=0, azim=-180,
                                        prot_color='green',
                                        file_name='2prot_1nm_y_R8nm',
                                        file_ext=file_ext,
                                        fig_size=fig_size)
    



if __name__ == "__main__":

    files_nb = ['2prot_1nm_z_R8nm.png', '2prot_1nm_x_R8nm.png', '2prot_1nm_y_R8nm.png']
    files_paper =['2prot_1nm_z_R8nm.pdf', '2prot_1nm_x_R8nm.pdf', '2prot_1nm_y_R8nm.pdf']

    status_nb = file_exist(files_nb)
    status_paper = file_exist(files_paper)

    
    if status_nb == False: 
        print('This can take couple of minutes, please wait while images for '
            'notebook report are produced.')
        main()
    
    if status_paper == False:
        print('This can take couple of minutes, please wait while images for '
            'paper are produced.')
        main(paper=True)

    elif (status_nb and status_paper) == True:
        print('Visualizations for notebook and paper already exist! If you want' 
        'to generate them again, please delete the existing ones.')


