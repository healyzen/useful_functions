"""
This is numeric python converted into a class with numeric methods. Requires Sympy
jesse.naumanen@tuni.fi
"""
import sympy
x = sympy.symbols("x")

class MathFunction:
    """
    This is a class for mathematical functions like x**2, f(x)
    :param f_string: function in string format, which gets converted into a function
    """
    def __init__(self,f_string):
        self.__fexp = sympy.sympify(f_string)

    def value(self, value_of_x):
        """
        a method for value substitution
        :param value_of_x: x to be subbed
        :return:
        """
        return self.__fexp.subs(x, value_of_x)

    def derivative(self):
        derivative = MathFunction(sympy.diff(self.__fexp))
        return derivative

    def newtons_method(self,x_val = 1, decimal_places = 4, iteration_limit = 50):
        """
        a method that calculates a real root of a function using Newton's method
        :param x_val: starting value of x
        :param decimal_places: number of decimal required in answer
        :param iteration_limit: max number of iteration allowed
        :return: value of x and f at final iteration
        """
        f = self.__fexp
        df = self.derivative()
        def new_newton_value(vf, vdf, vx):
            """
            newtons method main formula
            :param vf: value of function
            :param vdf: value of derivative
            :param vx: value of x
            :return: new value of x
            """
            return float(vx - (vf / vdf))
        decimals = 1 * 10 ** -decimal_places
        # starting values
        f_val = self.value(x_val)
        print(f"The value of f at x0 = {f_val:.20f} ~ {f_val:.3f}")
        print()
        i = 0  # the nth iteration
        # main while loop
        while f_val > decimals or f_val < -decimals:
            if iteration_limit <= i:  # iteration limiter
                print("\nFinished, iteration limit reached")
                print(f"x is {x_val:.10f} ~ {x_val:.3f}")
                print(f"f(x) is {f_val:.10f} ~ {f_val:.3f}")
                return 0
            else:
                i += 1
                print(f"{i}. iteration")
                f_val = self.value(x_val)
                df_val = df.value(x_val)
                print(f"The value of x is: {x_val:.10f}")
                print(f"The value of f is: {f_val:.10f}")
                x_val = new_newton_value(f_val, df_val, x_val)
                print()

        print("Finished:")
        print(f"x is {x_val:.20f} ~ {x_val:.3f}")
        print(f"f(x) is  {f_val:.20f} ~ {f_val:.3f}")
        return x_val,f_val

def main():
    f = MathFunction("4*x + sqrt(x**3)")
    f.newtons_method(10,6,100)

if __name__ == "__main__":
    main()
