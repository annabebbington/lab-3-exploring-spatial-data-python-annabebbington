Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'''
Anna Bebbington
10/4/20
This code creates a new geodatabase and adds feature classes in a folder to that geodatabase. The inputs are the feature classes in the workspace, and the outputs are
the geodatabase and those same feature classes in the geodatabse. Each feature class is made up of multiple files, and this code moves all files associated with a feature class
'''
# imports arcpy and import env from arcpy
>>> import arcpy
>>> from arcpy import env
# .overwriteOutput allows the script to overwrite existing files
>>> env.overwriteOutput = True
# uses env to set workspace using filepath to folder with shapefile data
>>> env.workspace = "C:\\Programming_for_GIS\\Lab_3_Exploring_Spatial_Data\\"
# creates a new geodatabase in the folder indicated by the file path name
>>> arcpy.CreateFileGDB_management("C:\\Programming_for_GIS\\Lab_3_Exploring_Spatial_Data\\Results\\", "NM.gdb")
<Result 'C:\\Programming_for_GIS\\Lab_3_Exploring_Spatial_Data\\Results\\NM.gdb'>
# creates a list from the feature classes
>>> fclist = arcpy.ListFeatureClasses()
# uses a forloop to iterate through the list of feature classes. A new variable (fcdesc) is created for the items in the list, which includes the feature
# class information. Each feature class in the list is added to the newly created geodatabase, using the file base name
>>> for fc in fclist:
	fcdesc = arcpy.Describe(fc)
	arcpy.CopyFeatures_management(fc, "C:\\Programming_for_GIS\\Lab_3_Exploring_Spatial_Data\\Results\\NM.gdb" + fcdesc.basename)
'''
<Result 'C:\\Programming_for_GIS\\Lab_3_Exploring_Spatial_Data\\Results\\amtrak_stations.shp'>
<Result 'C:\\Programming_for_GIS\\Lab_3_Exploring_Spatial_Data\\Results\\cities.shp'>
<Result 'C:\\Programming_for_GIS\\Lab_3_Exploring_Spatial_Data\\Results\\counties.shp'>
<Result 'C:\\Programming_for_GIS\\Lab_3_Exploring_Spatial_Data\\Results\\new_mexico.shp'>
<Result 'C:\\Programming_for_GIS\\Lab_3_Exploring_Spatial_Data\\Results\\railroads.shp'>
'''

