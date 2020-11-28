#
# This class will retrieve data from this weather station website:
#
#     https://thingspeak.com/channels/12397/
#
# The available data fields look like this:
#
# WeatherStation Channel Feed:	JSON XML CSV
# Field 1 Data: Wind Direction (North = 0 degrees)	JSON XML CSV
# Field 2 Data: Wind Speed (mph)	JSON XML CSV
# Field 3 Data: % Humidity	JSON XML CSV
# Field 4 Data: Temperature (F)	JSON XML CSV
# Field 5 Data: Rain (Inches/minute)	JSON XML CSV
# Field 6 Data: Pressure ("Hg)	JSON XML CSV
# Field 7 Data: Power Level (V)	JSON XML CSV
# Field 8 Data: Light Intensity	JSON XML CSV
#



import pandas as pd
print('Pandas version ', pd.__version__)

class WeatherGetter:
    def __init__(self):
        self.dataURL = ''

    def buildURL(self, index, numPoints):
        # build the URL to access which is https://thingspeak.com/channels/12397/fields/4/.csv?results=1000
        self.dataURL = 'https://api.thingspeak.com/channels/12397/fields/'
        self.dataURL += str(index)
        self.dataURL += '.csv?results='         # we want .csv output
        self.dataURL += str(numPoints)     # number of points to get
        #print(self.dataURL)

    def getData(self, index, numPoints):
         # build the url, then read the data from the URL into a dataframe using pandas, and return the series
        self.buildURL(index, numPoints)
        dataFrame = pd.read_csv(self.dataURL)
        return dataFrame
        # index = 'field' + str(index)  # creating column index 'fieldX' for the data
        # data = dataFrame[index]  # indexing into the file for the column index
        # return data


