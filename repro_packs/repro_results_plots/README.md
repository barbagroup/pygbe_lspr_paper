# Reproducibility results-plots package

This directory contains the necessary information to reproduce the results figures 
and visualizations of the paper: PyGBe-LSPR—Computational nanoplasmonics for biosensing applications

To be able to reproduce these results the user needs python and Jupyter notebooks. 

Python libraries needed:
- `numpy` (used by author 1.15.4)
- `matplotlib` (used by author 2.2.2)

**Folder descriptions**:

* `BSA_silver_NP_LSPR_response` : Reproduce LSPR sensitivy results
* `convergence_analyses` : Reproduce convergence analyses results
* `spherical_silver_NP_verification` : Reproduce isolated spherical silver nanoparticle verification results.
* `visualizations` : Reproduce the images of the sensor with the proteins (`pdfs` for the paper and `png` for notebook report in BSA_silver_NP_LSPR_response)


Each directory, except `visualizations`, contains a Jupyter notebooks that will display the results as well as reproduce the plots as they appear in the paper.After running the a notebook the paper-version of the plots will be saved under the results directory located at the same level than the notebook. In the directories of the form results/original the user can find the original plots used in the paper. 


 To reproduce the `visualizations` run:

`$ python visualizations.py`

The resulting figures will be under the folder `figures`. The user can find the original version under  `figures/original/`


