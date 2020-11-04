Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'''
Anna Bebbington
10/4/20
This code checks that specific shapefile exisits in a workspace 
'''
# import arcpy and env to set workspace to file with shapefiles
>>> import arcpy
>>> from arcpy import env
>>> env.workspace = "C:\\Programming_for_GIS\\Lab_3_Exploring_Spatial_Data\\Data-Lab_3_Exploring_Spatial_Data"
# define the variable shape_exists, and use .Exists to check whether a specific shapefile exists in the folder
# set as the workspace. It is a boolean expression (returns true/false)
>>> shape_exists = arcpy.Exists("cities.shp")
>>> print shape_exists
True
# .Exists is not case sensitive. still returns true 
>>> shape_exists = arcpy.Exists("CITIES.SHP")
>>> print shape_exists
True
>>> 
