"""
A little program to practice with numpy, pandas, matplotlib
"""

# Import all the packages we'll need

import WeatherGetter as wg
import numpy as np
import matplotlib.pyplot as plt

def processWind(direction, speed):
    # We want the maximum wind speed in each direction
    pass

def main():
    numDashes = 40
    print()
    print('-' * numDashes)
    print('--- numpy, pandas, matplotlib ---')
    print('-' * numDashes)
    print()

    numPoints = 5000

    # Get the last numPoints wind direction (field1) and speed (field2) samples
    dirName = 'Direction(deg)'
    speedName = 'Velocity(mph)'
    getter = wg.WeatherGetter()
    windDataFrame = getter.getData(1, numPoints)
    speedDF = getter.getData(2, numPoints)

    # Get rid of the 'entry_id' column in both dataframes
    del windDataFrame['entry_id']
    del speedDF['entry_id']

    # Insert the wind velocity column as 'field2'
    windDataFrame.insert( loc=len(windDataFrame.columns), column='field2', value=speedDF['field2'])

    # Rename the columns to something that makes sense
    windDataFrame.rename(columns={'created_at': 'Date/Time', 'field1': dirName, 'field2': speedName}, inplace=True)
    print(windDataFrame)

    # Plot it, both polar and x vs y
    title = "Plot of Wind direction vs. Speed in Natick, MA using the past {} data points".format(numPoints)
    ax = plt.subplot(211, projection='polar')
    ax.set_theta_offset(np.pi / 2)
    tickLabels = ['N', 'NW', 'W', 'SW', 'S', 'SE', 'E', 'NE']
    tickValues = []
    for i in range(8):
        tickValues.append(i*(np.pi/4))
    ax.set_xticks(tickValues)
    ax.set_xticklabels(tickLabels)
    plt.title(title)
    # Plot polar to show direction and speed
    # convert dirData to radians for use in a polar plot. Note we're using numpy-style notation here:
    # operation is performed on the entire array
    # rad = deg * pi/180, but we need to reverse direction for polar plot, so rad = -deg*pi/180
    radData = ((-windDataFrame[dirName] * np.pi) / 180)
    # add 2pi to make sure it's positive
    radData += (2*np.pi)
    plt.plot(radData, windDataFrame[speedName], 'g.')

    # Then plot linear
    ax2 = plt.subplot(212)
    plt.xlabel(speedName)
    plt.ylabel(dirName)
    plt.plot(windDataFrame[speedName], windDataFrame[dirName], 'rx')
    tickLabels = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    tickValues = [0, 45, 90, 135, 180, 225, 270, 315]
    ax2.set_yticks(tickValues)
    ax2.set_yticklabels(tickLabels)

    plt.show()
    print('\nDone!')


if __name__ == '__main__':
    main()
