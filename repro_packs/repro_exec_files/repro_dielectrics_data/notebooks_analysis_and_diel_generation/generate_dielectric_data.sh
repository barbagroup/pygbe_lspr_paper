### Silver

python scripts/generate_dielectric.py -s 3800 -e 4000 -n 41 -d silver_water_raw-data/silver_JC72_ang.txt -o ../dielectrics_data_results/wave_ang_silver_diel_3800-4000.txt

### Water

python scripts/generate_dielectric.py -s 3800 -e 4000 -n 41 -d silver_water_raw-data/water_HQ72_ang.txt -o ../dielectrics_data_results/wave_ang_water_diel_3800-4000.txt

#For simulations of LSPR response (wavelength range 382-387 nm)

### Silver

python scripts/generate_dielectric.py -s 3820 -e 3870 -n 21 -d silver_water_raw-data/silver_JC72_ang.txt -o ../dielectrics_data_results/wave_ang_silver_diel_3820-3870.txt

### Water

python scripts/generate_dielectric.py -s 3820 -e 3870 -n 21 -d silver_water_raw-data/water_HQ72_ang.txt -o ../dielectrics_data_results/wave_ang_water_diel_3820-3870.txt

### Bovine Serum Albumin (BSA)
#In this case the wavelength are passed in `nm` but the output will be in Angstrom since we needed in this unit for simulation purposes.

python scripts/generate_protein_dielectric.py -s 382 -e 387 -n 21 -o ../dielectrics_data_results/wave_ang_prot_diel_3820-3870.txt
