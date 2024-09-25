"""
A collection of mathematical functions, without module dependence
Currently mainly statistical functions
jesse.naumanen@tuni.fi
"""
def calculate_median(list):
    """
    median calculator
    :param list: list of values
    :return: list median
    """
    list = sorted(list)
    length = len(list) #list length
    if length % 2 == 0: #if_even
        median = (list[int(length/2)] + list[int(length/2) - 1])/2
        return median
    else: #if_odd
        median = list[int(length/2)]
        return median

def calculate_average(list):
    """
    average calculator
    :param list: list of values
    :return: list average
    """
    length = len(list)
    sum_value = 0
    for value in list:
        sum_value += value
    average = sum_value/length
    return average

def calculate_variance(list):
    """
    list variance and std_dev calculator
    :param list: list of values
    :return: variance and stdDev of list
    """
    length = len(list) #list length
    average = calculate_average(list) #average
    sum_list = 0 #variance sum
    for value in list:
        sum_list += (value-average)**2
    variance = (1/(length-1))*sum_list #variance
    std_deviation = variance**0.5 #sqrt of variance
    return variance, std_deviation

def min_max(list):
    """
    list min & max
    :param list: a list of values
    :return: list min and max
    """
    list = sorted(list)
    return list[0], list[-1] #list first and last index

def statistic_list_result(list):
    """
    list statistics printer, dependent on other functions within this module
    :param list: list of values
    :return: list statistics
    """
    list_min, list_max = min_max(list)
    median = calculate_median(list)
    mean = calculate_average(list)
    variance, deviation = calculate_variance(list)
    print(F"Minimum:   {list_min:.2f} cm")
    print(F"Maximum:   {list_max:.2f} cm")
    print(F"Median:    {median:.2f} cm")
    print(F"Mean:      {mean:.2f} cm")
    print(F"Deviation: {deviation:.2f} cm")

def main():
    print("This is pyStat")

if __name__ == "__main__":
    main()
