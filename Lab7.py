#!/usr/bin/env python3
#
# Lab 07 - CIS 133Y - Fall 2020
# Dave Johnson
#
# A program to practice with numpy, pandas, and matplotlib.
#
# We get weather data from an internet weather station (in this case wind speed and direction),
# then plot it, both polar and cartesion.
#
# I'm not sure I used enough numpy commands for the assignment, but I'm not too worried, I'm only a
# senior audit. This sure was fun learning a little about these packages, and matplotlib in particular.
#

# Import all the packages we'll need
import numpy as np
import pandas as pd
import matplotlib as mp
import matplotlib.pyplot as plt

# show versions
print('NumPy version ', np.__version__)
print('Pandas version ', pd.__version__)
print('MatPlotLib version ', mp.__version__)

# -------------------------------------------
# A few "globals", strictly for convenience.

# The number of points to retrieve and plot
numPoints = 5000

#  The column names, used as indices later
dirName = 'Direction(deg)'
speedName = 'Velocity(mph)'

# -------------------------------------------
# All the subroutines

# Build the url to retrieve data and return it as a string
# We need to specify the field to get, the format (.csv), and the number of points
def buildURL(index):
    dataURL = 'https://api.thingspeak.com/channels/12397/fields/'
    dataURL += str(index)
    dataURL += '.csv?results='  # we want .csv output
    dataURL += str(numPoints)  # number of points to get
    return dataURL

# Get the weather data at the specified index
def getWeatherData(index):
    # build the url, then read the data from the URL into a dataframe using pandas, and return it
    theURL = buildURL(index)
    dataFrame = pd.read_csv(theURL)
    return dataFrame

# Combine the direction and speed dataframes into one, with a column for each value,
# and rename the columns nicely
def makeWindDF(dirDF, speedDF):
     # First insert the wind velocity column as 'field2' at the far right
    dirDF.insert(loc=len(dirDF.columns), column='field2', value=speedDF['field2'])

     # Rename the columns to something human-happy
    dirDF.rename(columns={'created_at': 'Date/Time', 'entry_id': 'EntryID', 'field1': dirName, 'field2': speedName}, inplace=True)
    return dirDF

def retrievePlottableWindData():
    # Get the last numPoints  of both wind direction (field1) and wind speed (field2),
    # and combine into one nice table, then return it.
    dirDF = getWeatherData(1)
    speedDF = getWeatherData(2)
    return makeWindDF(dirDF, speedDF)

def plotWindData(windDF):
    # Plot it, both polar and x vs y
    title = "Plot of Wind direction vs. Speed in Natick, MA using the past {} data points".format(numPoints)
    plt.title(title)

    # -----------------------
    # First the polar plot
    ax = plt.subplot(211, projection='polar')

    # set the ticks to show the compass points, with North at the top
    # Note: since the polar plot is positive anti-clockwise, the labels are
    # reversed from their "normal" clockwise sequence
    ax.set_theta_offset(np.pi / 2)
    tickLabels = ['N', 'NW', 'W', 'SW', 'S', 'SE', 'E', 'NE']
    tickValues = []
    for i in range(8):
        tickValues.append(i*(np.pi/4))
    ax.set_xticks(tickValues)
    ax.set_xticklabels(tickLabels)

    # convert direction data to radians for the polar plot. Note we're using numpy implicitly here:
    # arithmetic is performed on the entire array in one statement
    # radians = deg * pi/180, and we need to reverse direction, so
    thetaData = ((-windDF[dirName] * np.pi) / 180)

    # add 2pi to make sure it's positive, then plot it with green dots
    # todo is this necessary?
    thetaData += (2*np.pi)
    plt.plot(thetaData, windDF[speedName], 'gx', alpha=0.25)

    # -----------------------
    # Then the linear plot, with red x's, and approriate ticks and labels
    ax2 = plt.subplot(212)
    plt.xlabel(speedName)
    plt.ylabel(dirName)

    tickLabels = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    tickValues = [0, 45, 90, 135, 180, 225, 270, 315]
    ax2.set_yticks(tickValues)
    ax2.set_yticklabels(tickLabels)
    plt.plot(windDF[speedName], windDF[dirName], 'rx', alpha=0.25)

    # finally, save the plot as a .pdf and show it
    plt.savefig("Wind Plot.pdf") # , bbox_inches="tight"
    plt.show()


def main():
    numDashes = 50
    print()
    print('-' * numDashes)
    print('--- practice with numpy, pandas, and matplotlib ---')
    print('-' * numDashes)
    print()

    # Get data and plot it
    windDF = retrievePlottableWindData()
    plotWindData(windDF)
    print('Done!')

if __name__ == '__main__':
    main()
