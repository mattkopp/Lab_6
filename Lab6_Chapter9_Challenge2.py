#Matt Koppelman
#GIS501
#10/29/2014
#Lab 6 - Chapter 9 - Challenge 1


import arcpy
from arcpy import env
env.workspace = "H:/UWTacoma/GIS501/Lab_6/Exercise09"

rasterlist = arcpy.ListRasters()

arcpy.CreateFileGDB_management("H:/UWTacoma/GIS501/Lab_6/Exercise09/Results", "raster.gdb")

for raster in rasterlist:
	desc = arcpy.Describe(raster)
	name = desc.baseName
	finallocation = "H:/UWTacoma/GIS501/Lab_6/Exercise09/Results/raster.gdb/" + name
	arcpy.CopyRaster_management(raster, finallocation)