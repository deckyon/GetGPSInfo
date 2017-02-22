#!/usr/bin/env python

# Set up the different libraries used in the script.
from OmegaExpansion import oledExp
import time
import json
import os

# Initialize and clear the OLED screen.
oledExp.setVerbosity(0)
oledExp.setTextColumns()
oledExp.driverInit()

# Draw the header on the OLED.
oledExp.setCursor(0, 0)
oledExp.write("+-------------------+")
oledExp.setCursor(1, 0)
oledExp.write("| Current GPS Info: |")
oledExp.setCursor(2, 0)
oledExp.write("+---------+---------+")

# Check for the existence of the text file.  If it does not exist, write that and exit.
# You will need to change the location of the txt file path to match where you have yours located.
if os.path.getsize('/smb/scripts/gpsinfo.txt') == 0:
	oledExp.setCursor(4, 0)
	oledExp.write("GPS Info doesnt seem")
	oledExp.setCursor(5, 0)
	oledExp.write("to exist.")
	oledExp.setCursor(6, 0)
	oledExp.write("Check GPSInfo file.")
	exit()

# Read the information gathered from the GPS expansion
# Make sure to change the directory to match where this file lives.
with file('/smb/scripts/gpsinfo.txt', 'r') as gpsfile:
	gpsinfo = json.load(gpsfile)

# Check to see that the GPS expansion actually pulled the location
# If not, write that and exit, if so, display info on OLED and exit.
if gpsinfo.has_key('signal'):
	oledExp.setCursor(4, 0)
	oledExp.write("No GPS signal found")
	oledExp.setCursor(5, 0)
	oledExp.write("Please try later!")
elif gpsinfo.has_key('latitude'):
	oledExp.setCursor(3, 0)
	oledExp.write("Latitude  | "+gpsinfo['latitude'])
	oledExp.setCursor(4, 0)
	oledExp.write("Longitude | "+gpsinfo['longitude'])
	oledExp.setCursor(5, 0)
	oledExp.write("Elevation | "+gpsinfo['elevation'])
	oledExp.setCursor(6, 0)
	oledExp.write("Course    | "+gpsinfo['course'])
	oledExp.setCursor(7, 0)
	oledExp.write("Speed     | "+gpsinfo['speed'])

exit()
