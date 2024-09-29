"""
pyStat converted to a class of StatList with pyStats functions as methods
jesse.naumanen@tuni.fi
"""
class StatList:
    def __init__(self,list):
        self.__statlist = list

    def calculate_median(self):
        """
        median calculator
        :param list: list of values
        :return: list median
        """
        list = sorted(self.__statlist)
        length = len(list)  # list length
        if length % 2 == 0:  # if_even
            median = (list[int(length / 2)] + list[int(length / 2) - 1]) / 2
            return median
        else:  # if_odd
            median = list[int(length / 2)]
            return median

    def calculate_average(self):
        """
        average calculator
        :param list: list of values
        :return: list average
        """
        list = self.__statlist
        length = len(list)
        sum_value = 0
        for value in list:
            sum_value += value
        average = sum_value / length
        return average

    def calculate_variance(self):
        """
        list variance and std_dev calculator
        :param list: list of values
        :return: variance and stdDev of list
        """
        list = self.__statlist
        length = len(list)  # list length
        average = self.calculate_average()  # average
        sum_list = 0  # variance sum
        for value in list:
            sum_list += (value - average) ** 2
        variance = (1 / (length - 1)) * sum_list  # variance
        std_deviation = variance ** 0.5  # sqrt of variance
        return variance, std_deviation

    def min_max(self):
        """
        list min & max
        :param list: a list of values
        :return: list min and max
        """
        list = sorted(self.__statlist)
        return list[0], list[-1]  # list first and last index

    def statistic_list_result(self):
        """
        list statistics printer, dependent on other functions within this module
        :param list: list of values
        :return: list statistics
        """
        list_min, list_max = self.min_max()
        median = self.calculate_median()
        mean = self.calculate_average()
        variance, deviation = self.calculate_variance()
        print(F"Minimum:   {list_min:.2f} cm")
        print(F"Maximum:   {list_max:.2f} cm")
        print(F"Median:    {median:.2f} cm")
        print(F"Mean:      {mean:.2f} cm")
        print(F"Deviation: {deviation:.2f} cm")

#main for testing purposes
def main():
    print("This is pyStat")
    list = StatList([1,2,3,4,5,6,7,8,9,10])
    list.statistic_list_result()

if __name__ == "__main__":
    main()