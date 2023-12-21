# Conversion from .CZI to .SVS for whole slide images

I generated this script to convert whole folders containing Carl Zeiss Files (.czi) to Leica whole slide image files (.svs).

This script takes all of the .czi files contained in a selected folder and converts them to .svs files, saved in a chosen folder. I then use these files for analysis in 
[HistoLens](https://cmilab.nephrology.medicine.ufl.edu/software/histolens-2/) from the Sarder Lab at the University of Florida. Feel free to use and adjust this script as necessary for your
personal needs.

An important note is that, at least with my 40x images, conversion takes *1-2 hours per scene*. It's a long time. I usually run these overnight. Since the files are so large, I usually compress the folders,
too, once I am done converting them.
