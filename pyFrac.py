"""
This is pyFrac, a class for symbolic calculations of fractions
jesse.naumanen@tuni.fi
"""

class Fraction:
    """
    This class represents one single fraction
    that consists of a numerator and denominator.
    """

    def __init__(self, numerator, denominator):
        """
        initializer, using attributes numerator and denominator
        :param numerator: int, the fraction's numerator
        :param denominator: int, the fraction's denominator
        """

        # value checks for valid values
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # denominator cannot be zero
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def __lt__(self, other):
        """
        comparison operator
        :param other: the other fraction to be compared
        """
        return self.__numerator*other.__denominator < other.__numerator*self.__denominator

    def __str__(self):
        """
        this is string type support
        """
        if self.__numerator * self.__denominator < 0:
            sign = "-"
        else:
            sign = ""
        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"

    def return_string(self):
        """
        This is the string version of the target fraction
        : prints a string interpretation of the fraction
        """
        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"

    def simplify(self):
        """
        this function simplifies a fraction using the greatest common divisor function
        """
        gcd = greatest_common_divisor(self.__numerator, self.__denominator)
        self.__numerator = self.__numerator // gcd
        self.__denominator = self.__denominator // gcd

    def complement(self):
        """
        This is a function for making the complement of a fraction
        """
        numerator = - self.__numerator
        denominator = self.__denominator
        return Fraction(numerator,denominator)

    def reciprocal(self):
        numerator = self.__denominator
        denominator = self.__numerator
        return Fraction(numerator, denominator)

    def multiply(self,other_fraction):
        """
        This is a function that multiplies the target fraction with another fraction
        :param other_fraction: the fraction that gets multiplied with the target fraction
        """
        new_numerator = self.__numerator * other_fraction.__numerator
        new_denominator = self.__denominator * other_fraction.__denominator
        fraction_product = Fraction(new_numerator,new_denominator)
        return fraction_product.simplify()

    def divide(self, other_fraction):
        """
        This function divides a fraction using the multiply and reciprocal methods
        :param other_fraction: the dividing fraction
        """
        new_numerator = self.__numerator * other_fraction.reciprocal().__numerator
        new_denominator = self.__denominator * other_fraction.reciprocal().__denominator
        quotient = Fraction(new_numerator,new_denominator)
        return quotient.simplify()

    def add(self,other_fraction):
        """
        this is a method to add two fractions together
        :param other_fraction: the other fraction to be summed
        """
        new_denominator = self.__denominator*other_fraction.__denominator
        new_numerator = self.__numerator*other_fraction.__denominator + other_fraction.__numerator*self.__denominator
        fraction_sum = Fraction(new_numerator,new_denominator)
        return fraction_sum.simplify()

    def deduct(self,other_fraction):
        """
        this method deducts a fraction from the target fraction
        :param other_fraction: the fraction to be deducted
        """
        new_denominator = self.__denominator*other_fraction.__denominator
        new_numerator = self.__numerator*other_fraction.__denominator - other_fraction.__numerator*self.__denominator
        new_fraction = Fraction(new_numerator, new_denominator)
        return new_fraction.simplify()

def greatest_common_divisor(a, b):
    """
    This function calculates the greatest common divisor for a pair of values
    :param a: the first value
    :param b: the second value
    """
    while b != 0:
        a, b = b, a % b
    return a

def main():
    print("this is pyFrac")

if __name__ == "__main__":
    main()
