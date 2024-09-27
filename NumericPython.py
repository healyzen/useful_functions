"""
A collection of numeric methods for python, using sympy
Currently only newtons method available
jesse.naumanen@tuni.fi
"""
import sympy
x = sympy.symbols("x") #symbolic x, used for most function in this file.

def debug(function,derivative,value_x,value_f,decimal_places,decimals,iteration_limit,iteration):
    """
    debug function for testing function values
    :return: debug value to console
    """
    print("printing debug info...\n")
    print("ff on", function)
    print("dff on", derivative)
    print("xi on", value_x)
    print("fa on", value_f)
    print("xdesi on", decimal_places)
    print("desi on", decimals)
    print("kr on", iteration_limit)
    print("itr on", iteration)
def function_value(function,value_of_x):
    """
    a functions value subs
    :param function: target function
    :param value_of_x: x to be subbed
    :return:
    """
    return function.subs(x, value_of_x)
def newtons_method():
    """
    a function that calculates a real root of a function using Newton's method
    :return:
    """
    str_expr = input("Give a target function (i.e. x**2): ") or "x**2"
    function = sympy.sympify(str_expr)
    derivative_of_function = sympy.diff(function)

    def new_newton_value(vf,vdf,vx):
        """
        newtons method main formula
        :param vf: value of function
        :param vdf: value of derivative
        :param vx: value of x
        :return: new value of x
        """
        return float(vx - (vf / vdf))

    #answer decimal places
    decimal_places = int(input("Input the amount of decimal places needed (std is 0.000): ") or 4)
    decimals = 1 * 10 ** -decimal_places

    #starting values
    value_of_x = float(input("Give a starting value (std is 1): ") or 1)
    value_f = function_value(function,value_of_x)
    print(f"The value of f at x0 = {value_f:.20f} ~ {value_f:.3f}")

    iteration_limit = int(input("Iteration limit (std is 50): ") or 50)
    print()
    i = 0 #the nth iteration
    #main while loop
    while value_f > decimals or value_f < -decimals:
        if iteration_limit <= i:  #iteration limiter
            print("\nFinished, iteration limit reached")
            print(f"x is {value_of_x:.10f} ~ {value_of_x:.3f}")
            print(f"f(x) is {value_f:.10f} ~ {value_f:.3f}")
            return 0
        else:
            i += 1
            print(f"{i}. iteration")
            value_f = float(function_value(function,value_of_x))
            value_df = float(function_value(derivative_of_function,value_of_x))
            print(f"The value of f is: {value_f:.10f}")
            print(f"The value of x is: {value_of_x:.10f}")
            value_of_x = new_newton_value(value_f, value_df, value_of_x)
            print()

    print("Finished:")
    print(f"x is {value_of_x:.20f} ~ {value_of_x:.3f}")
    print(f"f(x) is  {value_f:.20f} ~ {value_f:.3f}")

def main():
    newtons_method()

if __name__ == "__main__":
    main()
