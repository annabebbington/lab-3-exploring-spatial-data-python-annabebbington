Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'''
Anna Bebbington
10/4/20
This code is for use in ArcPy. This code creates a variable from a shapefile.
The user can use this script to explore information about the shapefile  including data type, file path, and more detailed referencce information.   
'''
>>> myshape = arcpy.Describe("C:\\Programming_for_GIS\\Lab_3_Exploring_Spatial_Data\\Data-Lab_3_Exploring_Spatial_Data\\cities.shp")
>>> myshape.dataType
# u'ShapeFile'

>>> 
# create new variable mylayer, linking to a layer in the current map document
>>> mylayer = arcpy.Describe("cities") # got a runtime error with "cities.shp", so I had to remove the .shp
# outputs the data type of the variable
>>> mylayer.dataType
# u'FeatureLayer'
# outputs the dataset type of the variable
>>> mylayer.datasetType
# u'FeatureClass'
# outputs the catalog path of the variable
>>> mylayer.catalogPath
# u'C:\\Programming_for_GIS\\Lab_3_Exploring_Spatial_Data\\Data-Lab_3_Exploring_Spatial_Data\\cities.shp'
# outputs the base name of the variable
>>> mylayer.basename
# u'cities'
# outputs the file name of the variable
>>> mylayer.file
# u'cities.shp'
# outputs whether the data set is versioned or not (boolean)
>>> mylayer.isVersioned
# False
# outputs the shapefile type of the variable
>>> mylayer.shapeType
# u'Point'
# outputs the spatial reference information of the variable. Different spatial reference properties can then be accessed individually
>>> mylayer.spatialReference
# <geoprocessing spatial reference object object at 0x1E063728>
# outputs the name of the spatial reference for the variable
>>> mylayer.spatialReference.name
# u'GCS_North_American_1983'
# outputs the type of  spatial reference system for the variable
>>> mylayer.spatialReference.type
# u'Geographic'
# outputs the smallest and largest X and Y coordinates for the variable
>>> mylayer.spatialReference.domain
# u'-400 -400 400 400'
>>> 
