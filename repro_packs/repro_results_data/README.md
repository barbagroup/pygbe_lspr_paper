# Reproducibility data package

This directory contains four different folders that reproduce the
data for the article: PyGBe-LSPR—Computational nanoplasmonics for biosensing applications 

- To be able to run the scripts the user needs:

1. Install PyGBe. 

Installation can be done via docker or from source. Dockerfile and instructions for source installation are available in the Github code repository https://github.com/barbagroup/pygbe

2. Download input problem folders data from [zenodo](https://zenodo.org/record/2511600#.XB6o48tKjeQ)

Download zip file and extract in desired location. If using docker container, data should be available in the container.

**Important note**:
When passing input problem folder path to run scripts the path must end in /:

For example: if `pygbe_lspr_problems` was downloaded in the directory 

`home/Downloads`, then the path will be:

`home/Downloads/pygbe_lspr_problems/`


## Directories content description.

**Name of directory**: `repro_dielectrics_data`

`noteboooks_analysis_and_diel_generation`

- Contains three Jupyter notebooks with the analysis of the dielectrics data from the papers that were extracted. These notebooks allowed us to decide the interpolation strategy used to generate the data we needed. 

Notebooks: - `water_data_analysis.ipynb`
           - `silver_data_analysis.ipynb`
           - `bsa_data_analysis.ipynb`

- Contains a Jupyter notebook and a bash script that can both be used to generate the dielectric data used in our computations.

The user can either run the bash script:

`$ bash generate_dielectric_data.sh`

or open the `generate_dielectric_data.ipynb` notebook and press run all.

In both cases the results will be saved under the directory:

`repro_dielectrics_data/dielectrics_data_results/`

The original results used in our simulations are under:

`repro_dielectrics_data/dielectrics_data_results/original`

*Note*: We use experimental data from Johnson and Christy, 1972 (silver) and Hale and Querry, 1972 (water) to perform the interpolation. These data is located under the directory `silver_water_raw_data`. 

**Name of directory**: `repro_BSA_silver_NP_LSPR_response_data`

This folder contains the necessary scripts to reproduce all the
results related to sensitivity calculations. 

* `dielectrics_data/`

This subdirectory contains the dielectric data needed to perform the computations. The reproducible package associated with this data is under `repro_dielectrics_data` directory.

* `Cext_two_bsa_x_results/original` 

This subdirectory contains the original results of the LSPR response of the Silver nanoparticle with no proteins and with the presence of
two BSA at a distance of 1 nm at each side of the x-axis. It also contains a `txt` file reporting the run-time for the problem (all times are in seconds) 

To reproduce this result the user should in the directory scripts and run the following shell command:

`$ python Cext_wave_dist_prot_sensor_x.py -if full_path_where_input_problem_folder_is_located`

In an Nvidia K40c GPU card the run-time is approximately 6 hours.

After running the script the user can find the results in the directory

`Cext_two_bsa_x_results/`


* `Cext_two_bsa_y_results/original`

This subdirectory contains the original results of the LSPR response
of the Silver nanoparticle with no proteins and with the presence of
two BSA at a distance of 1 nm at each side of the y-axis. It also contains a `txt` file reporting the run-time for the problem (all times are in seconds) 

To reproduce this result the user should be inside the directory scripts and run the following shell command:

`$ python Cext_wave_dist_prot_sensor_y.py -if full_path_where_input_problem_folder_is_located`

In an Nvidia K40c GPU card the run-time is approximately 5.2 hours.

After running the script the user can find the results in the directory

`Cext_two_bsa_y_results/`

* `Cext_variation_with_distance_two_bsa_z_results/original`

This subdirectory contains the original results of the LSPR response
of the Silver nanoparticle with no proteins and with the presence of
two BSA at a distances of 0.5 nm, 1 nm, and 2 nm at each side of the z-axis. It also contains a `txt` file reporting the run-time for the problem (all times are in seconds) 

To replicate this result the user should be inside the directory scripts and run the following shell command:

`$ python Cext_wave_dist_prot_sensor_z.py -if full_path_where_input_problem_folder_is_located`

In an Nvidia K40c GPU card the run-time is approximately 16 hours.

After running the script the user can find the results in the directory

`Cext_variation_with_distance_two_bsa_z_results/`


**Name of directory**: `repro_convergence_analysis_data`

Under the subdirectory scripts the user can find the scripts to run convergence computations. 

To compute the isolated spherical silver sphere run:

`$ python single_sphere_Ag.py -if full_path_where_input_problem_folder_is_located`

The user can find the results under the directory:

`repro_convergence_analysis_data/results/sph_sensor_Ag/`

The format of this result is a pickle file. To inspect this file, in a python console run: 

```python
>>> import pickle
>>> with open('sph_sensor_Ag_convergence.pickle', 'rb') as f:
        res_dict = pickle.load(f)
>>> res_dict 
```

The original results are under:

`repro_convergence_analysis_data/results/sph_sensor_Ag/original`

To compute the bsa-sensor convergence :

`$ python bsa_sph_sensor.py -if full_path_where_input_problem_folder_is_located`

The user can find the results under the directory:

`repro_convergence_analysis_data/results/sphere_bsa/`

The format of this result is a pickle file. To inspect this file, in a python console run: 
```python
>>> import pickle
>>> with open('sphere_bsa_convergence.pickle', 'rb') as f:
        res_dict = pickle.load(f)
>>> res_dict 
```
The original results are under:

`repro_convergence_analysis_data/results/sphere_bsa/original`


**Name of directory**: `repro_silver_spherical_NP_verification_data`

Under the subdirectory scripts the user can find the scripts to run verification. To perform this computation run:

`$ python Cext_wave.py -if full_path_where_input_problem_folder_is_located`

The results will go to the directory:

`repro_silver_spherical_NP_verification_data/results/`

The original results are under:

repro_silver_spherical_NP_verification_data/results/original 

*Note*: The directory `data/` contains necessary dielectric data to perform the verification runs. 




