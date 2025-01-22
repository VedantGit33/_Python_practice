# Factorial Program using function
import math
def calculate_factorial(num):

    if num == 0:           # Base case
        return 1

    else:
        return num * math.calculate_factorial(num-1) # Recurssive function


def main():

    n = int(input("Enter a number:"))

    if n < 0 :
        print('Number is not valid')

    else:
        fact = calculate_factorial(n)
        print(f"Factorial of {n} is {fact}")

main()
