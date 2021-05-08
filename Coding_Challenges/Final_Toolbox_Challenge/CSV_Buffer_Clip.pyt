# Final Toolbox Challenge:
"""This toolbox take an XY Table and converts it to a shapefile, then buffers said shapefile based on user inputs (size, units)
The buffer is then used to clip against another shapefile...
In this case the tool uses the stranded species CSV file, buffers by 1,000 feet and tells us which marinas are within that proximity.
This could be useful for stranded species counts, and reporting for volunteers who are interested in typical stranding locations."""


import arcpy

# Define and name your tool:
# This tool uses a csv to shapefile script, buffer, and clip
# Tool 1:
class Toolbox(object):
    def __init__(self):
        self.label = "CSV Buffer Clip"
        self.alias = "FinalToolChallenge"
        self.tools = [convert_CSV_to_Shapefile,buffer, clip]

class convert_CSV_to_Shapefile(object):
    def __init__(self):
        self.label = "Convert CSV to shapefile \ Part 1"
        self.description = "Convert a CSV file to a Shapefile to use in ArcPro"

        self.canRunInBackground = False
# Set the Parameters for the conversion:

    def getParameterInfo(self):
        params = []
        # This is a required input of a Table , not necessarily a CSV so it can be changed based on what the user needs
        input_CSV = arcpy.Parameter(name="input_CSV",
                                          displayName="Input CSV file to be Converted",
                                          datatype="DEFile",
                                          parameterType="Required",
                                          direction="Input")
        params.append(input_CSV)

        output = arcpy.Parameter(name="output",
                                 displayName="Output",
                                 datatype="DEShapeFile",
                                 parameterType="Required",  # Required|Optional|Derived
                                 direction="Output",  # Input|Output
                                 )
# Give the output a value so the same file can be used in future scripts within the toolbox:
        output.value = r"C:\PYthon_Class\Coding_Challenges\Final_Toolbox\Toolbox1\CSV_to_Shape_Output.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(output)
        return params

    def isLicensed(self):
        return True

    def updateParameters(self, parameters):
        return

    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):
        input_CSV = parameters[0].valueAsText
        output = parameters[1].valueAsText


        arcpy.management.XYTableToPoint(in_table=input_CSV,
                                        out_feature_class=output,
                                        x_field="",
                                        y_field="",
                                        z_field="",
                                        coordinate_system="GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119521E-09;0.001;0.001;IsHighPrecision")

        return

# Tool 2:
class buffer(object):
    def __init__(self):
        self.label = "Buffer Zone for Boaters \ Part 2"
        self.description = "Buffer the newly created shapefile to determine the " \
                           "danger zones for boaters"

        self.canRunInBackground = False

    def getParameterInfo(self):
# Once again define your  buffer and use output from above for this input:
        params = []
        buffer = arcpy.Parameter(name="buffer_data",
                                   displayName="Input Shapefile created from CSV Table",
                                   datatype="DEShapeFile",
                                   parameterType="Required",
                                   direction="Input")
        buffer.value = r"C:\PYthon_Class\Coding_Challenges\Final_Toolbox\Toolbox1\CSV_to_Shape_Output.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(buffer)

        buffer_output = arcpy.Parameter(name="buffer_output",
                                      displayName="Buffer Output",
                                      datatype="DEFeatureClass",
                                      parameterType="Required",
                                      direction="Output")
        buffer_output.value = r"C:\PYthon_Class\Coding_Challenges\Final_Toolbox\Toolbox1\Buffer_output.shp"
        params.append(buffer_output)
# The user will be able to enter the desired buffer size
        buffer_size = arcpy.Parameter(name="buffer_size",
                                        displayName="Size of Buffer in Meters or Feet",
                                        datatype="Field",
                                        parameterType="Required",
                                        direction="Input")
        params.append(buffer_size)
# The user will be able to enter the desired buffer unit whether in feet or meters:
        buffer_unit = arcpy.Parameter(name="buffer_unit",
                                      displayName="Buffer Unit (Feet or Meters)",
                                      datatype="Field",
                                      parameterType="Required",
                                      direction="Input")

        buffer_unit.columns = [['GPString', 'Field']]
        buffer_unit.values = [['']]
        buffer_unit.filters[0].list = ['Feet', 'Meters']

        params.append(buffer_unit)

        return params

    def isLicensed(self):
        return True

    def updateParameters(self, parameters):
        return

    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):
        buffer = parameters[0].valueAsText
        buffer_output = parameters[1].valueAsText
        buffer_size = parameters[2].valueAsText
        buffer_unit = parameters[3].valueAsText

        arcpy.Buffer_analysis(in_features=buffer,
                              out_feature_class=buffer_output,
                              buffer_distance_or_field=buffer_size + " " + buffer_unit,
                              line_side="FULL",
                              line_end_type="ROUND",
                              dissolve_option="ALL",
                              dissolve_field=[],
                              method="PLANAR")
        return

# Tool 3:
# Use the Clip feature to clip the marinas that intersect with the chosen buffer size from stranded species above:
class clip(object):
    def __init__(self):
        self.label = "Clip Stranded Species to Marinas \  Part 3"
        self.description = "Clip buffered shapefile from " \
                           "new input shapefile"
        self.canRunInBackground = False

    def getParameterInfo(self):

        params = []
# Input the swmarinas shapefile here:
        marinas = arcpy.Parameter(name="marinas_shapefile",
                                        displayName="Shapefile to be clipped",
                                        datatype="DEFeatureClass",
                                        parameterType="Required",
                                        direction="Input")

        buffer_info = arcpy.Parameter(name="buffer_output",
                                      displayName="Buffered Shapefile",
                                      datatype="DEFeatureClass",
                                      parameterType="Required",
                                      direction="Input")
        buffer_info.value = r"C:\PYthon_Class\Coding_Challenges\Final_Toolbox\Toolbox1\Buffer_output.shp"
        params.append(buffer_info)



        params.append(marinas)

        clipped_output = arcpy.Parameter(name="clipped_marinas",
                                            displayName="Clipped Output",
                                            datatype="DEShapeFile",
                                            parameterType="Required",
                                            direction="Output")
        clipped_output.value = r"C:\PYthon_Class\Coding_Challenges\Final_Toolbox\Toolbox1\clipped_output.shp"
        params.append(clipped_output)

        return params

    def isLicensed(self):
        return True

    def updateParameters(self, parameters):
        return

    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):
        marinas = parameters[0].valueAsText
        buffer_info = parameters[1].valueAsText
        clipped_output = parameters[2].valueAsText

        arcpy.Clip_analysis(in_features=buffer_info,
                            clip_features=marinas,
                            out_feature_class=clipped_output,
                            cluster_tolerance="")

        return






