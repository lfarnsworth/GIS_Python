# Midterm Tool Challenge
# In this assignment, you are instructed to produce a small script tool
# that takes advantage of arcpy and Python. You will need to provide example data,
# and the code should run on all PC's. The tool needs to manipulate a dataset across
# three different processes, for example, extracting, modifying and exporting data.
# The exact workflow is entirely up to yourself.
# You are expected to take 3-4 hours on this coding assignment,
# and you should deposit your code and example files within a Github repository for feedback and grading.
#

# The criteria are:
#
# Cleanliness of code (10 points)
# Functionality (10 points)
# Appropriate use of documentation (10 points)
# Depth of processing operation (10 points)
# In addition, you must provide example data and
# minimize the amount of editing a user must make in order for the program to run (10 points).

"""
Overview:
This script creates a 1 km buffer around all public access points that are within 500 feet of a sewage outflow site.
This is useful for people attempting to avoid swimming near raw sewage
Possible use for this would be a local newspaper, community website, or mobile app based on GPS
Swimming in these areas should be avoided after a heavy rainstorm.

Inputs:
This script uses three datasets:
    Coastal waters (used to clip buffer zones)
    Sewage Outflow (potential source of contaminants)
    Public Access Locations (possibly affected swimming areas)
Public Access Sites: https://opendata.arcgis.com/datasets/37634e3cfd3843229fffa35c3e0ff43d_0.zip?geometry=%7B%22xmin%22%3A-73.79%2C%22ymin%22%3A41.154%2C%22xmax%22%3A-69.222%2C%22ymax%22%3A41.873%2C%22type%22%3A%22extent%22%2C%22spatialReference%22%3A%7B%22wkid%22%3A4326%7D%7D
Coastal Waters: https://opendata.arcgis.com/datasets/5a7ca8e875724e0b9d5538db5f0ca997_0.zip?geometry=%7B%22xmin%22%3A-76.088%2C%22ymin%22%3A40.669%2C%22xmax%22%3A-66.953%2C%22ymax%22%3A42.112%2C%22type%22%3A%22extent%22%2C%22spatialReference%22%3A%7B%22wkid%22%3A4326%7D%7D
RIPDES: https://opendata.arcgis.com/datasets/1c38fe33c5324ffd9a4f412b96564d0a_0.zip?geometry=%7B%22xmin%22%3A-73.79%2C%22ymin%22%3A41.232%2C%22xmax%22%3A-69.223%2C%22ymax%22%3A41.951%2C%22type%22%3A%22extent%22%2C%22spatialReference%22%3A%7B%22wkid%22%3A4326%7D%7D
(Data is also provided in Github)

Outputs:
The script outputs a CSV file of all the affected public access points that are dangerously close to waste outflows.
"""


import arcpy
import os
arcpy.env.overwriteOutput = True
# I updated this to utilize os.path.join - it should work now!
# Modify base_folder to fit your environment:
base_folder = r"C:\YOUR_FILE_PATH_HERE"
arcpy.env.workspace = os.path.join(base_folder, "Data")

# Process #1
# Select all waste sites within 500 feet of a public shoreline access point
Shoreline_Selection = arcpy.management.SelectLayerByLocation(
    in_layer = os.path.join(base_folder, "Data/RIPDES_Sanitary_Waste_Sites.shp"),
    overlap_type = "INTERSECT",
    select_features = os.path.join(base_folder, "Data/Public_Shoreline_Access.shp"),
    search_distance = "500 Feet",
    selection_type = "NEW_SELECTION",
    invert_spatial_relationship = "NOT_INVERT"
)

# Process #2
# 1 km buffer around the above selected waste sites.
No_Swim_Areas_Shapefile = "No_Swim.shp"
Polluted_Shoreline_Buffer = arcpy.analysis.Buffer(
    in_features = Shoreline_Selection,
    out_feature_class = No_Swim_Areas_Shapefile,
    buffer_distance_or_field = "1 Kilometers",
    line_side = "FULL",
    line_end_type = "ROUND",
    dissolve_option = "NONE",
    dissolve_field = [],
    method = "PLANAR"
)

# Process #3
# Clip buffer to coastal waters (removes buffer from land area)
Toxic_Water_Sites = "Toxic_Water_Sites.shp"
arcpy.analysis.Clip(
    in_features = No_Swim_Areas_Shapefile,
    clip_features = os.path.join(base_folder, "Data/Coastal_Waters.shp"),
    out_feature_class = Toxic_Water_Sites,
    cluster_tolerance = ""
)

# Process #4
# Select intersecting buffer and public access sites to generate a list of sites that should be avoided for swimming
Toxic_Swim_Sites = arcpy.management.SelectLayerByLocation(
    in_layer = os.path.join(base_folder, "Data/Public_Shoreline_Access.shp"),
    overlap_type = "INTERSECT",
    select_features = Toxic_Water_Sites,
    search_distance = "500 Feet",
    selection_type = "NEW_SELECTION",
    invert_spatial_relationship = "NOT_INVERT"
)

# Process #5
# Save the above selection to a shapefile, useful for validating in ArcPro
Toxic_Swim_Sites_Shapefile = "Toxic_Swim_Sites.shp"
arcpy.management.CopyFeatures(
    in_features = Toxic_Swim_Sites,
    out_feature_class = Toxic_Swim_Sites_Shapefile
)

# Process #6
# Generate a csv file from the attribute table that selects only the areas where you want to avoid swimming
arcpy.TableToTable_conversion(Toxic_Swim_Sites_Shapefile, base_folder, "contaminated_swim_sites.csv")

# Process #7
# Output a list to the console window of the potential sites to avoid
print('The following output is a list of the Public Access Sites you\'d want to avoid swimming in after a heavy rainstorm: ')
with arcpy.da.SearchCursor(Toxic_Swim_Sites_Shapefile, ['TOWN1', 'NAME', 'PRIMEUSE']) as List_Of_Contaminated_Swim_Sites_cursor:
    for List_Of_Contaminated_Swim_Sites_row in List_Of_Contaminated_Swim_Sites_cursor:
        print(List_Of_Contaminated_Swim_Sites_row)
