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
    numDashes = 10
    print()
    print('-' * numDashes)
    print('--- numpy, pandas, matplotlib ---')
    print('-' * numDashes)
    print()

    numPoints = 50

    # Get the last numPoints wind direction (field1) and speed (field2) samples
    getter = wg.WeatherGetter()
    windDataFrame = getter.getData(1, numPoints)
    speedDF = getter.getData(2, numPoints)
    del windDataFrame['entry_id']
    del speedDF['entry_id']
    print(windDataFrame)
    print(speedDF)

    #windDataFrame.set_index('created_at').join(speedDF.set_index('created_at'))
    print('\nJoining...\n')
    # windDataFrame.merge(speedDF['field2'])
    windDataFrame.join(speedDF['field2'], how='inner', lsuffix='_x', rsuffix='_y')
    print(windDataFrame)
#    windDataFrame.join(speedDF)

#     # index = 'field' + str(2)  # creating column index 'fieldX' for the data
#     # speedSeries = speedDF[index]  # indexing into the file for the column index
#     #
#     # # Append the column to the dataframe
#     # windDataFrame[index] = speedSeries
#
#
#     # print(speedData)
#     # print(dirData)
#
#     # Plot it
#     title = "Plot of Wind direction vs. Speed in Natick, MA using the past {} data points".format(numPoints)
#
#     # convert dirData to radians for use in a polar plot. Note we're using numpy-style notation here:
#     # operation is performed on the entire array
#     # rad = deg * pi/180, but we need to reverse direction for polar plot, so rad = -deg*pi/180
#     radData = (((dirData * -1) * np.pi) / 180)
#     # add 2pi to make sure it's positive
#     radData += (2 * np.pi)
#
# #    plt.polar(radData, speedData, 'rx')
#     plt.title(title)
#     # plt.xlabel('Speed (mph)')
#     # plt.ylabel('Direction')
#     plt.plot(speedData, dirData, 'rx')
#
#     plt.show()

    print('Done!')


if __name__ == '__main__':
    main()

    # def plotData(self, series, title = '', xLabel = '', yLabel = '', legend = [], fmt = ''):
    #     plt.plot(series)
    #
    #     # Step 4 Add details like title, labels, legend
    #     plt.title(title)
    #     plt.xlabel(xLabel)
    #     plt.ylabel(yLabel)
    #     plt.legend(legend)
    #
    # def plotDoubleData(self, series1, series2, title = '', xLabel = '', yLabel = '', legend = [], fmt = ''):
    #     plt.plot(series1, series2)
    #
    #     # Step 4 Add details like title, labels, legend
    #     plt.title(title)
    #     plt.xlabel(xLabel)
    #     plt.ylabel(yLabel)
    #     plt.legend(legend)
    #
    # def plotPolar(self, series1, series2, title = '', xLabel = '', yLabel = '', legend = [], fmt = ''):
    #     plt.polar(series1, series2, fmt)
    #
    #     # for i in range(len(series1)):
    #     #     plt.polar(series1[i], series2[i])
    #
    #     # Step 4 Add details like title, labels, legend
    #     plt.title(title)
    #     plt.xlabel(xLabel)
    #     plt.ylabel(yLabel)
    #     plt.legend(legend)
    #
    # def showPlots(self):
    #     # Step 5 - Show Plot and Save if needed
    #     plt.savefig("weather.png", dpi=300, bbox_inches="tight")
    #     plt.show()
    #
