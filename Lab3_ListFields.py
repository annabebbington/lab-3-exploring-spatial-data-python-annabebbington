Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'''
Anna Bebbington
10/4/20
This code creates a list of the informational fields associated with a specific shapefile (cities), and uses a for loop to print out the field name and data type.
'''
# imports arcpy and imports env from arcpy
>>> import arcpy
>>> from arcpy import env
# .overwriteOutput allows the script to overwrite existing files
>>> env.overwriteOutput = True
# uses env to set workspace using filepath to folder with shapefile data 
>>> env.workspace = "C:\\Programming_for_GIS\\Lab_3_Exploring_Spatial_Data\\"
# creates a new list of fields in the cities shapefile
>>> fieldlist = arcpy.ListFields("C:\\Programming_for_GIS\\Lab_3_Exploring_Spatial_Data\\Data-Lab_3_Exploring_Spatial_Data\\cities.shp")
# for loop iterates through each object in the list, and prints the name of the field, a space, and the data type of the field. 
>>> for field in fieldlist:
	print field.name + " " + field.type

'''	
FID OID
Shape Geometry
CITIESX020 Double
FEATURE String
NAME String
POP_RANGE String
POP_2000 Integer
FIPS55 String
COUNTY String
FIPS String
STATE String
STATE_FIPS String
DISPLAY SmallInteger
'''
 
