"""
Coding Challenge 5
For this coding challenge, I want you to practice the heatmap generation that we went through in class, but this time obtain your own input data, and I want you to generate heatmaps for TWO species.

You can obtain species data from a vast array of different sources, for example:

obis - Note: You should delete many columns (keep species name, lat/lon) as OBIS adds some really long strings that don't fit the Shapefile specification.
GBIF
Maybe something on RI GIS
Or just Google species distribution data
My requirements are:

The two input species data must be in a SINGLE CSV file, you must process the input data to separate out the species (Hint: You can a slightly edited version of our CSV code from a previous session to do this), I recommend downloading the species data from the same source so the columns match.
Only a single line of code needs to be altered (workspace environment) to ensure code runs on my computer, and you provide the species data along with your Python code.
The heatmaps are set to the right size and extent for your species input data, i.e. appropriate fishnet cellSize.
You leave no trace of execution, except the resulting heatmap files.
You provide print statements that explain what the code is doing, e.g. Fishnet file generated.
"""

# Database taken from OBIS : http://ipt.env.duke.edu/archive.do?r=zd_945&v=1.4
# Mystic_Stranded_Species_Loggerhead_harp.csv was generated by deleting superfluous columns in occurence.txt in excel and saving as CSV
# This challenge will focus on the Loggerhead and Harp Seal data.


import arcpy
import csv
import os
arcpy.env.overwriteOutput = True
# Set your workspace to the directory where you are storing your files
arcpy.env.workspace = r"C:\Data\Students_2021\Farnsworth\Coding_Challenges\Challenge5\workspace"
file_name = "Mystic_Stranded_Species_ANSI.csv"

# create empty list to populate with the csv file:
stranded_species_list = []

# use for loop to create csv with two stranded species : Loggerhead & Harp Seal (Both found in vernacularName column)
with open(arcpy.env.workspace + '\\' + file_name) as stranded_csv:
    next(stranded_csv)
    for row in csv.reader(stranded_csv):
        if row[7] not in stranded_species_list:
            stranded_species_list.append(row[7])
stranded_csv.close()

print('stranded_species_list: ' + str(stranded_species_list))
#species_1 = stranded_species_list[0]
#species_2 = stranded_species_list[1]
species_1 = 'Loggerhead'
species_2 = 'Harp Seal'
print('species_1: ' + species_1)
print('species_2: ' + species_2)
stranded_species_list = [species_1, species_2]

# Separate out the two species from the csv file and create two files:
with open(arcpy.env.workspace + '\\' + file_name) as species_types:
    row_count_i = 0
    for row in csv.reader(species_types):
        if row_count_i == 0:
            file_1 = open(arcpy.env.workspace + '\\' + species_1 + ".csv", "w")
            file_1.write(",".join(row))
            file_1.write("\n")
            file_2 = open(arcpy.env.workspace + '\\' + species_2 + ".csv", "w")
            file_2.write(",".join(row))
            file_2.write("\n")
        if row[7] == species_1:
            file_1 = open(arcpy.env.workspace + '\\' + species_1 + ".csv", "a")
            file_1.write(",".join(row))
            file_1.write("\n")
        if row[7] == species_2:
            file_2 = open(arcpy.env.workspace + '\\' + species_2 + ".csv", "a")
            file_2.write(",".join(row))
            file_2.write("\n")
        row_count_i = row_count_i + 1
species_types.close()
file_1.close()
file_2.close()

print("Separate species files created")


# convert the csv files into shapefiles and save them:
for species in stranded_species_list:
    in_Table = species + ".csv"
    print('in_Table: ' + in_Table + " : " + species)
    x_coords = "decimalLongitude"
    y_coords = "decimalLatitude"
    z_coords = ""
    out_Layer = "poopie"
    saved_Layer = species + ".shp"
    spRef = arcpy.SpatialReference(4326)  # 4326 == WGS 1984
    lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)

    arcpy.CopyFeatures_management(lyr, saved_Layer)
    if arcpy.Exists(saved_Layer):
        print("Created file successfully")
    else:
        print("Error")



    arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)
    outFeatureClass = species + "_fishnet.shp"  # Name of output fishnet

    desc = arcpy.Describe(saved_Layer)
    XMin = desc.extent.XMin
    XMax = desc.extent.XMax
    YMin = desc.extent.YMin
    YMax = desc.extent.YMax

# Set the cell size and coordiantes for the fishnet:
    originCoordinate = str(XMin) + " " + str(YMin)  # Left bottom of our point data
    yAxisCoordinate = str(XMin) + " " + str(YMin + 1.0)  # This sets the orientation on the y-axis, so we head north
    cellSizeWidth = "0.05"
    cellSizeHeight = "0.05"
    numRows =  ""  # Leave blank, as we have set cellSize
    numColumns = "" # Leave blank, as we have set cellSize
    oppositeCorner = str(XMax) + " " + str(YMax)  # i.e. max x and max y coordinate
    labels = "NO_LABELS"
    templateExtent = "#"  # No need to use, as we have set yAxisCoordinate and oppositeCorner
    geometryType = "POLYGON"  # Create a polygon, could be POLYLINE

    arcpy.CreateFishnet_management(outFeatureClass, originCoordinate, yAxisCoordinate,
                               cellSizeWidth, cellSizeHeight, numRows, numColumns,
                               oppositeCorner, labels, templateExtent, geometryType)
# check to see that fishnet was created:
    if arcpy.Exists(outFeatureClass):
        print("Created Fishnet file successfully!")
    # Create fishnet:
    target_features = species + "_fishnet.shp"
    join_features = species + ".shp"
    out_feature_class = species + "_heatmap.shp"
    join_operation = "JOIN_ONE_TO_ONE"
    join_type = "KEEP_ALL"
    field_mapping = ""
    match_option = "INTERSECT"
    search_radius = ""
    distance_field_name = ""
# #
    arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
                           join_operation, join_type, field_mapping, match_option,
                           search_radius, distance_field_name)
# Use print statement to check if heatmap was created
    if arcpy.Exists(out_feature_class):
        print("Created heatmap file successfully")

#Delete all unnecessary files:
    print("Deleting extra files")
    arcpy.Delete_management(target_features)
    arcpy.Delete_management(join_features)
species_types.close()
file_1.close()
file_2.close()

for species in stranded_species_list:
    print("Deleting: " + species + ".csv")
    os.remove(arcpy.env.workspace + '\\' + species + ".csv")

print("deleted extra files")

