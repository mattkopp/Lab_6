#Matt Koppelman
#GIS501
#10/29/2014
#Lab 6 - Chapter 9 - Challenge 1

#Notes: Could not get get script to run correctly unless the raster files were located within a geodatabase.  If the script for challenge 2 is run first, this script works.

import arcpy
from arcpy import env
env.workspace = r"H:\UWTacoma\GIS501\Lab_6\Exercise09\Results\raster.gdb"
arcpy.env.overwriteOutput = True


if arcpy.CheckExtension("Spatial") == "Available":
	arcpy.CheckOutExtension("Spatial")
	
	
elev = arcpy.Raster("Elevation")
lc = arcpy.Raster("landcover")


slope = arcpy.sa.Slope(elev)
aspect = arcpy.sa.Aspect(elev)


modslope = ((slope > 5) & (slope < 20))
southaspect = ((aspect > 150) & (aspect < 270))
forest = ((lc == 41) | (lc == 42) | (lc ==43))


finalraster = (modslope & southaspect & forest)
finalraster.save(r"H:\UWTacoma\GIS501\Lab_6\Exercise09\Results\raster.gdb\Challenge1")


arcpy.CheckInExtension("Spatial")

