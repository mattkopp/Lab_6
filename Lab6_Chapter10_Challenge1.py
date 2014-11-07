#Matt Koppelman
#GIS501
#10/29/2014
#Lab 6 - Chapter 10 - Challenge 1


import arcpy

mxd = r"H:\UWTacoma\GIS501\Lab_6\Exercise10\Austin_TX.mxd"
mapdoc = arcpy.mapping.MapDocument(mxd)

parksdf = arcpy.mapping.ListDataFrames(mapdoc, "Parks")[0]
parklayer = arcpy.mapping.ListLayers(mapdoc, "parks", parksdf)[0]
dflist = arcpy.mapping.ListDataFrames(mapdoc)


for df in dflist:
	if df.name <> "Parks":
		arcpy.mapping.AddLayer(df, parklayer, "BOTTOM")

mapdoc.save()

	
del mapdoc



