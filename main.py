"""
A little program to practice with numpy, pandas, matplotlib
"""

# Import all the packages we'll need

import WeatherGetter as wg
import WeatherPlotter as wp
import numpy as np

def main():
    numDashes = 50
    print()
    print('-' * numDashes)
    print('--- numpy, pandas, matplotlib ---')
    print('-' * numDashes)
    print()

    numPoints = 20

    # Get the last numPoints wind direction (field1) and speed (field2) samples
    getter = wg.WeatherGetter()
    dirData = getter.getData(1, numPoints)
    speedData = getter.getData(2, numPoints)
    # print(speedData)
    # print(dirData)

    title = "Plot of Wind speed in Natick, Ma using past {} data points".format(numPoints)
    plotter = wp.WeatherPlotter()
#    plotter.plotData(speedData, title, "Daily values", "Wind speed (mph)")
    # convert dirData to radians
    radData = []
    for dir in dirData:
        rad = (((dir * -1) * np.pi) / 180) + (2 * np.pi)
        radData.append(rad)

    plotter.plotPolar(radData, speedData, title, "Daily values", "Wind speed (mph)")

    print('Done!')

if __name__ == '__main__':
    main()
