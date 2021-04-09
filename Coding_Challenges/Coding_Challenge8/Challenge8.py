
"""Our coding challenge this week follows from the last exercise that we did in class
during Week 8 where we worked with functions.
Convert some of your earlier code into a function.

The only rules are:

1) You must do more than one thing to your input to the function,and
2) the function must take two arguments or more.You must also,
3) provide a zip file of example data within your repo.

Plan the task to take an hour or two, so use one of the simpler examples from our past classes."""


# Taken from coding challenge 6 (Rewrote for loop as a function & added verbosity option) :

import arcpy
import os

# Make sure you can overwrite your output:
arcpy.env.overwriteOutput = True

#  Create a list of months we have in the dataset for 2015
list_months = ["02", "04", "05", "07", "10", "11"]

#  Set the output directory for NDVI files:
workingDirectory = r"C:\PYthon_Class\Coding_Challenges\Coding_Challenge8\Step_3_data_lfs"
if not os.path.exists(workingDirectory):
    os.mkdir(workingDirectory)

from arcpy.sa import *

"""
This function takes three arguments:
1: workingDirectory - (string) os path containing data, TIFs will be outputted here as well.
2: month - (string) - month represented as a number; leading 0 required.
3: verbosity - (boolean) - True enables print outputs, False won't.

It finds the B4 and B5 raster TIF files for the given month,
then calculates the NVDI Raster and outputs a new TIF to the working directory.
The verbosity switch enables/disables printing for quiet output.
"""

def generate_NVDI_TIF(workingDirectory, month, verbosity):
    arcpy.env.workspace = os.path.join(workingDirectory, "2015" + str(month))
    listRasters = arcpy.ListRasters("*", "TIF")
    if verbosity:
        print(listRasters)

    listRasterRed = [x for x in listRasters if "B4" in x]
    listRasterNIR = [x for x in listRasters if "B5" in x]

    if verbosity:
        print(("Raster Red: ") + str(listRasterRed))
        print(("Raster NIR: ") + str(listRasterNIR))


    # Equation for NVDI:
    output_raster = (Raster(listRasterNIR) - Raster(listRasterRed)) / (Raster(listRasterNIR) + Raster(listRasterRed))
    output_raster.save(os.path.join(workingDirectory, "2015" + str(month) + "_NDVI.tif"))

    # Print to make sure it exists:
    if verbosity:
        print(output_raster)

# End generate_NVDI_TIF function

# MAIN
# use a for loop to find the months in the dataset using * and TIF as query search terms
for month in list_months:
    generate_NVDI_TIF(workingDirectory, month, False)

