"""
A collection of mathematical functions, without module depencencies
Currently mainly statistical functions
jesse.naumanen@tuni.fi
"""
def calculateMedian(list):
    """
    median calculator
    :param list: list of values
    :return: list median
    """
    list = sorted(list) #järjestää listan suuruusjärjestykseen
    lenght = len(list) #listan pituus
    if lenght % 2 == 0: # jos parillinen määrä arvoja
        median = (list[int(lenght/2)] + list[int(lenght/2) - 1])/2
        return median
    else: # jos pariton määrä arvoja
        median = list[int((lenght)/2)]
        return median

def calculateAverage(list):
    """
    average calculator
    :param list: list of values
    :return: list average
    """
    lenght = len(list)
    sumValue = 0
    for value in list:
        sumValue += value
    average = sumValue/lenght
    return average

def calculateVariance(list):
    """
    list variance and stdev calculator
    :param list: list of values
    :return: variance and stdDev of list
    """
    lenght = len(list) #list length
    average = calculateAverage(list) #average
    sumList = 0 #variance sum
    for value in list:
        sumList += (value-average)**2
    variance = (1/(lenght-1))*sumList #variance
    stdDeviation = variance**0.5 #sqrt of variance
    return variance, stdDeviation

def minmax(list):
    """
    list min & max
    :param list: a list
    :return: list min and max
    """
    list = sorted(list) #järjestää listan
    return list[0], list[-1] #palauttaan listan ensimmäisen ja viimeisen arvo

def statisticResult(list):
    """
    list statistics printer, dependent on other functions within this module
    :param list: list of values
    :return: list statistics
    """
    min, max = minmax(list)
    median = calculateMedian(list)
    mean = calculateAverage(list)
    variance, deviation = calculateVariance(list)
    print(F"Minimum:   {min:.2f} cm")
    print(F"Maximum:   {max:.2f} cm")
    print(F"Median:    {median:.2f} cm")
    print(F"Mean:      {mean:.2f} cm")
    print(F"Deviation: {deviation:.2f} cm")

def main():
    print("This is pyStat")

if __name__ == "__main__":
    main()
