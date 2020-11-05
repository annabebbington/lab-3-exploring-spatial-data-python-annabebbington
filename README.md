# LAB 3: EXPLORING SPATIAL DATA USING PYTHON


##  SCRIPTS INCLUDED IN THIS REPO
You will submit a file to your Github repo via Moodle. You will need to create your own `.py` files for the repo. *Be sure they all contain good comment headers!* Your repo should contain:
- `Lab3_shape_exists.py` - This code checks that specific shapefile exisits in a workspace.
- `Lab3_describing_data` – This code is for use in ArcPy. This code creates a variable from a shapefile. The user can use this script to explore information about the shapefile  including data type, file path, and more detailed referencce information. 
- `Lab3_list.py` – This code creates a list from the feature classes in the workspace. The code uses a for loop to iterate through each feature class in the list, and uses .Describe to print print out the name and data type of each item in the list. Print statements are used to make this information more readable.
- `Lab3_listcopy.py` - This code creates a new geodatabase and adds feature classes in a folder to that geodatabase. The inputs are the feature classes in the workspace, and the outputs are the geodatabase and those same feature classes in the geodatabse. Each feature class is made up of multiple files, and this code moves all files associated with a feature class
- `Lab3_listfields.py` - This code creates a list of the informational fields associated with a specific shapefile (cities), and uses a for loop to print out the field name and data type. 


