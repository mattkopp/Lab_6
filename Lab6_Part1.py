#Matt Koppelman
#GIS501
#10/29/2014
#Lab 6 - Part 1


import turtle

turtle.title("Tommy the Turtle - Shape Drawer")
turtle.shape("turtle")
turtle.color("green")
turtle.pencolor("green")

print "Welcome to Tommy the Turtle's Shape Drawer."  

sides = int(input("Please enter the number of sides for your shape: "))
length = 600 / sides
angle = 360 / sides
CoordList = []

if sides < 3:
	print "Please start over."
elif sides >= 3:
	for side in range(sides):
		turtle.forward(length)
		turtle.left(angle)
		CoordList.insert(0, turtle.position())


print "Time to create Tommy's shapefile!"

import arcpy
from arcpy import env
env.workspace = "H:/UWTacoma/GIS501/Lab_6"

fc = "TommysShape.shp"
sr = arcpy.SpatialReference("WGS 1984")

arcpy.CreateFeatureclass_management("H:/UWTacoma/GIS501/Lab_6", fc, "Polygon", "", "", "", sr)
cursor = arcpy.da.InsertCursor(fc, ["SHAPE@"])
array = arcpy.Array()


for x, y in CoordList:
	point = arcpy.Point(x,y)
	array.append(point)
polygon = arcpy.Polygon(array)
cursor.insertRow([polygon])

del cursor

print "Shapefile complete"