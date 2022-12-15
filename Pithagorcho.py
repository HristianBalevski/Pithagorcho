import time
from math import pi, sqrt
from time import asctime


def invalid_input():
    print('Invalid Input')


# The Euclidean algorithm is a way to find the greatest common divisor of two positive integers, a and b.
def euclidean_algorithm(a, b):

    c = a % b
    while c:
        a = b
        b = c
        c = a % b
    print(f"The GCD of the numbers is ", b, end='\n')


# The Fibonacci sequence is a set of integers that starts with a zero,
# followed by a one, then by another one, and then by a series of steadily increasing numbers.
# The sequence follows the rule that each number is equal to the sum of the preceding two numbers.
def fibonacci_sequence(number):
    f0 = 0
    f1 = 1

    if number <= 0:
        print("Please enter a positive integer")
    elif number == 1:
        print("Fibonacci sequence up to", number, ":")
        print(f1)
    else:
        print("Fibonacci sequence:")
        counter = 0
        fib_seq_in_result = []

        while counter < number:
            fib_seq_in_result.append(f0)
            result = f0 + f1

            f0 = f1
            f1 = result
            counter += 1
        print(", ".join([str(num) for num in fib_seq_in_result]))


# The general formula for converting from degrees to radians is to simply multiply the number of degrees by π180∘ .
def convert_radians_to_degrees(number):
    d = number * 180 / pi
    print(f'{d:.2f}')


# A prime number is a whole number greater than 1 with only two factors – themselves and 1.
# A prime number cannot be divided by any other positive integers without leaving a remainder, decimal or fraction.
def prime_or_not_prime(num):
    is_prime = True

    if num == 0 or num == 1:
        print(f'The number {num} is Not Prime')
    else:
        for i in range(2, int(sqrt(num) + 1)):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f'The number {num} is Prime')
        else:
            print(f'The number {num} is Not Prime')


# When we add two numbers, the result we get can be defined as the SUM.
def sum_numbers(num1, num2):
    result = num1 + num2
    print(result)


# Subtraction of two positive numbers can be either positive or negative.
# Subtraction of two negative numbers can be either positive or negative.
def subtract_numbers(n1, n2):
    result = n1 - n2
    print(result)


# In math, to multiply means to add equal groups. When we multiply, the number of things in the group increases.
def multiply(num1, num2):
    result = num1 * num2
    print(result)


# Division in maths is the process of breaking a number up into equal parts,
# and finding out how many equal parts can be made.
def divide(num1, num2):
    result = num1 / num2
    print(result)


# In mathematics, a percentage is a number or ratio that can be expressed as a fraction of 100.
# If we have to calculate percent of a number, divide the number by the whole and multiply by 100.
def convert_to_percent(n1, n2):

    if n1 >= n2 or n1 <= 0 or n2 <= 0:
        print('Wrong Input!')
    else:
        result = ((n1 * 25) / (n2 * 25)) * 100
        print(f'{result}%')


print('Hello, I am Pithagocrho and I am here to help you!')
print()
print('''Press 1 for Euclidean Algorithm: 
Press 2 for Fibonacci Sequence: 
Press 3 for Convert Radians to Degrees:
Press 4 for Prime or Not Prime Number: 
Press 5 for Sum of Numbers:
Press 6 for Subtract Numbers:
Press 7 for Multiply Numbers:
Press 8 for Divide Numbers:
Press 9 for Decimal Fraction:
Press 10 to check Date and Time:
''')
while True:
    player = input('Please choose a number: ')
    if player in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'):

        if player == '1':
            a = int(input('Please choose an integer A: '))
            b = int(input('Please choose an integer B: '))

            euclidean_algorithm(a, b)

        elif player == '2':
            n = int(input('Please choose an integer number: '))

            fibonacci_sequence(n)

        elif player == '3':
            r = float(input('Please enter the radians: '))

            convert_radians_to_degrees(r)

        elif player == '4':
            n = int(input('Please enter and integer number: '))

            prime_or_not_prime(n)

        elif player == '5':
            a = float(input('Please enter a number: '))
            b = float(input('Please enter a number: '))

            sum_numbers(a, b)

        elif player == '6':
            a = float(input('Please enter a number: '))
            b = float(input('Please enter a number: '))

            subtract_numbers(a, b)

        elif player == '7':
            a = float(input('Please enter a number: '))
            b = float(input('Please enter a number: '))

            multiply(a, b)

        elif player == '8':
            a = float(input('Please enter a number: '))
            b = float(input('Please enter a number: '))

            divide(a, b)

        elif player == '9':
            print('Please enter two positive numbers. The second number must to be greater than the first!')
            x = float(input('Please enter a number: '))
            y = float(input('Please enter a number:'))

            convert_to_percent(x, y)

        # The asctime() function converts time, stored as a structure pointed to by time, to a character string.
        elif player == '10':
            print(time.asctime())
        else:
            invalid_input()

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == 'yes':
            continue
        elif next_calculation == "no":
            break
        else:
            invalid_input()
            break
    else:
        invalid_input()
