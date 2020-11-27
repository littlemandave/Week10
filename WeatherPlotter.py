import matplotlib as mp
import matplotlib.pyplot as plt

# show version of matplotlib
print('MatPlotLib version ', mp.__version__)

class WeatherPlotter:
    def __init__(self):
        pass

    def plotData(self, series, title = '', xLabel = '', yLabel = '', legend = []):
        plt.plot(series)

        # Step 4 Add details like title, labels, legend
        plt.title(title)
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.legend(legend)

        # Step 5 - Show Plot and Save if needed
        plt.savefig("weather.png", dpi=300, bbox_inches="tight")
        plt.show()

    def plotPolar(self, series1, series2, title = '', xLabel = '', yLabel = '', legend = []):
        plt.polar(series1, series2, 'o')

        # for i in range(len(series1)):
        #     plt.polar(series1[i], series2[i])

        # Step 4 Add details like title, labels, legend
        plt.title(title)
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.legend(legend)

        # Step 5 - Show Plot and Save if needed
        plt.savefig("weather.png", dpi=300, bbox_inches="tight")
        plt.show()

