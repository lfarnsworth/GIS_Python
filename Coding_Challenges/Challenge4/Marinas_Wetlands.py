# This program takes the two shapefiles below ( Marinas & Wetlands) and tells you which marinas are in wetlands using the Generate Near Table proximity tool.

# Datasets used :
# RI Marinas: http://data.rigis.org/FACILITY/swmarina.zip
# Wetlands: http://data.rigis.org/bio/NWI14.zip

# Load ArcGIS toolset functions
import arcpy

# Specify marina and wetland shapefile locations:
Marina_Shape_FilePath = r'C:\PYthon_Class\Coding_Challenges\challenge4\swmarina.shp'
Wetland_Shape_FilePath = r'C:\PYthon_Class\Coding_Challenges\challenge4\NWI14.shp'
# Specify output file for bad marinas:
Bad_Marinas_table = r'C:\PYthon_Class\Coding_Challenges\challenge4\BadMarinas.dbf'

# # Print Field Names
# print('Marina Fields: ')
# print([f.name for f in arcpy.ListFields(Marina_Shape_FilePath)])
# print('Wetlands Fields: ')
# print([f.name for f in arcpy.ListFields(Wetland_Shape_FilePath)])

count_of_marinas = 0
# Use data access function to count the number of marinas
with arcpy.da.SearchCursor(Marina_Shape_FilePath, ['FID']) as cursor:
    for row in cursor:
        count_of_marinas += 1
        #print(row)


print('There are ' + str(count_of_marinas) + ' total marinas in the given database')


# set required parameters
in_features = Marina_Shape_FilePath
near_features = Wetland_Shape_FilePath
out_table = Bad_Marinas_table

# optional parameters
search_radius = '1 Feet'
location = 'NO_LOCATION'
angle = 'NO_ANGLE'
closest = 'ALL'
closest_count = 1

print('\r\n')
print('Try generating the NEAR table:')
# Try generating near table if you've changed the search_radius
try:
    arcpy.GenerateNearTable_analysis(in_features, near_features, out_table, search_radius, location, angle, closest, closest_count)
    print('It worked!')
except:
    print('File wasn\'t made. Try deleting the existing .DBF')
    print('Moving on, but results might be out of sync')

print('\r\n')

count_of_badmarinas = 0
# Find FID in table and print list of necessary attributes (Name, Address, Town, Zip Code)
with arcpy.da.SearchCursor(Bad_Marinas_table, ['IN_FID']) as bad_marina_cursor:
    for bad_marina_row in bad_marina_cursor:
        count_of_badmarinas += 1
        with arcpy.da.SearchCursor(Marina_Shape_FilePath, ['NAME', 'ADDRESS', 'TOWN', 'ZIPCODE'], 'FID = ' + str(bad_marina_row[0])) as find_offending_marina_cursor:
            for matched_offender_row in find_offending_marina_cursor:
                print(matched_offender_row)
print('\r\n')
print('There are ' + str(count_of_badmarinas) + ' bad marinas in the given database.\r\nSend them nasty letters.')
