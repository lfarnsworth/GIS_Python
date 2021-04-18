"""In this coding challenge, your objective is to utilize the arcpy.da module to undertake some basic partitioning of
your dataset.
In this coding challenge, I want you to work with the Forest Health Works dataset from RI GIS
(I have provided this as a downloadable ZIP file in this repository).
Using the arcpy.da module (yes, there are other ways and better tools to do this),
I want you to extract all sites that have a photo of the invasive species (Field: PHOTO) into a new Shapefile,
and do some basic counts of the dataset. In summary, please addressing the following:

Count how many sites have photos, and how many do not (2 numbers), print the results.

Count how many unique species there are in the dataset, print the result.

Generate two shapefiles, one with photos and the other without."""


import arcpy
"""Step 1:
Count sites with photos"""
# Set your workspace:
arcpy.env.workspace = r'C:\PYthon_Class\Coding_Challenges\Coding_Challenge9\Data'
arcpy.env.overwriteOutput = True

# Define the shapefile that will be used as an input feature:
input_shp = r'C:\PYthon_Class\Coding_Challenges\Coding_Challenge9\RI_Forest_Health_Works_Project_Points_All_Invasives\RI_Forest_Health_Works_Project%3A_Points_All_Invasives.shp'

# Identify the fields you need to use to determine the sites with photos & create a list:
fields = ['Site', 'photo']

# This creates an expression to select all rows within the "photo" field that have a "y" input meaning there is a photo:
expression_photo = arcpy.AddFieldDelimiters(input_shp, "photo") + " = 'y'"  # Cleaner and easier to code
#  Define photo_count:
photo_count = 0
# Use SearchCursor in a for loop to find how many sites there are with photos:
with arcpy.da.SearchCursor(input_shp, fields, expression_photo) as cursor:
    for row in cursor:
# Print statement to show the Site name and 'y' for photo:
        print(u'{0}, {1}'.format(row[0], row[1]))
        photo_count = photo_count + 1


"""Step 2:
Count sites without photos"""

expression_no_photo = arcpy.AddFieldDelimiters(input_shp, "photo") + " <> 'y'"  # Cleaner and easier to code
#  Define photo_count:
No_photo_count = 0
# Use SearchCursor in a for loop to find how many sites there are without photos:
with arcpy.da.SearchCursor(input_shp, fields, expression_no_photo) as cursor:
    for row in cursor:
# Print statement to show the Site name and 'y' for photo:
        print(u'{0}, {1}'.format(row[0], row[1]))
        No_photo_count = No_photo_count + 1


# Print statement that counts the number of sites without photos:
print("There are " + str(No_photo_count) + " sites without photos in this shapefile.")
# Print statement that counts the number of sites with photo:
print("There are " + str(photo_count) + " sites with photos in this shapefile.")

"""Step 3
Count how many unique species there are in the dataset and print the result"""

unique_species_list = []
input = input_shp
field_2 = "Species"

with arcpy.da.SearchCursor(input, field_2) as cursor:
    for row in cursor:
        unique_species_list.append(row[0])

# Create a dict to populate with data from 'species' field. use for loop to count unique values:
unique_species_count = {}
for species in unique_species_list:
    if species not in unique_species_count.keys():
        unique_species_count[species] = 1
    else:
        unique_species_count[species] += 1

print("There are " + str(len(unique_species_count)) + " unique species in the shapefile")

"""Step 4
Generate two shapefiles, one with photos and one without"""


# Give your output file (shapefile) a name:
output_file_photo = "invasive_species_photo.shp"
Expression1 = "photo = 'y'"
arcpy.Select_analysis(input_shp, output_file_photo, Expression1)

# Check to make sure the output file was generated:
if arcpy.Exists(output_file_photo):
    print("Shapefile created successfully!")

# Now do the same thing for a second shapefile that does not contain the photos:
output_file_no_photo = "invasive_species_without_photo.shp"
Expression2 = "photo <> 'y'"
arcpy.Select_analysis(input_shp, output_file_no_photo, Expression2)

# Again, make sure it was actually generated:
if arcpy.Exists(output_file_no_photo):
    print("Shapefile without species photos created successfully!")

