Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'''
Anna Bebbington
10/4/20
This code creates a list from the feature classes in the workspace. The code uses a for loop to iterate through each
feature class in the list, and uses .Describe to print print out the name and data type of each item in the list. Print
statements are used to make this information more readable.  
'''
# imports arcpy and import env from arcpy
>>> import arcpy
>>> from arcpy import env
# uses env to set workspace using filepath to folder with shapefile data
>>> env.workspace = "C:\\Programming_for_GIS\\Lab_3_Exploring_Spatial_Data\\Data-Lab_3_Exploring_Spatial_Data"
# creates a new list of all the feature classes in the workspace
>>> fclist = arcpy.ListFeatureClasses()
# uses a for loop to iterate through the items in the list 
>>> for fc in fclist:
	fcdescribe = arcpy.Describe(fc) # creates a new variable with the .Describe information 
	print "Name: " + fcdescribe.name # prints the name of each feature class
	print "Data Type: " + fcdescribe.dataType # prints the data type of each feature class

'''	
Name: amtrak_stations.shp
Data Type: ShapeFile
Name: cities.shp
Data Type: ShapeFile
Name: counties.shp
Data Type: ShapeFile
Name: new_mexico.shp
Data Type: ShapeFile
Name: railroads.shp
Data Type: ShapeFile
'''

