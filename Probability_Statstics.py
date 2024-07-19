# Enter your code here. Read input from STDIN. Print output to STDOUT
from fractions import Fraction

def calculate_probability():
    P_White_from_X = Fraction(5, 9)
    P_Black_from_X = Fraction(4, 9)
    P_Black_from_Y_given_White_transferred = Fraction(6, 14)
    P_Black_from_Y_given_Black_transferred = Fraction(7, 14)

    P_Black_from_Y = (P_Black_from_X * P_Black_from_Y_given_Black_transferred +
                      P_White_from_X * P_Black_from_Y_given_White_transferred)

    return P_Black_from_Y

result = calculate_probability()

print(result)
