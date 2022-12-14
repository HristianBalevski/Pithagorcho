import time
from math import pi, sqrt
from time import asctime


def euclidean_algorithm(a, b):

    c = a % b
    while c:
        a = b
        b = c
        c = a % b
    print(f"The GCD of the numbers is ", b, end='\n')


def fibonacci_sequence(number):
    f0 = 1
    f1 = 1

    sequence = []
    for i in range(0, n - 1):
        f = f0 + f1
        f0 = f1
        f1 = f
        sequence.append(str(f1))
    print(', '.join(sequence))


def convert_radians_to_degrees(number):
    d = number * 180 / pi
    print(d)


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


def sum_numbers(num1, num2):
    result = num1 + num2
    print(result)


def subtract_numbers(n1, n2):
    result = n1 - n2
    print(result)


def multiply(num1, num2):
    result = num1 * num2
    print(result)


def divide(num1, num2):
    result = num1 / num2
    print(result)


def decimal_to_percent(n1, n2):

    if n1 >= n2 or n1 > 9 or n2 > 10:
        print('Wrong Input! The second number must to be greater than the first!')
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

player = int(input('Please choose a number: '))

if player == 1:
    a = int(input('Please choose an integer A: '))
    b = int(input('Please choose an integer B: '))

    euclidean_algorithm(a, b)

elif player == 2:
    n = int(input('Please choose an integer number: '))

    fibonacci_sequence(n)

elif player == 3:
    r = float(input('Please enter the radians: '))

    convert_radians_to_degrees(r)

elif player == 4:
    n = int(input('Please enter and integer number: '))

    prime_or_not_prime(n)

elif player == 5:
    a = float(input('Please enter a number: '))
    b = float(input('Please enter a number: '))

    sum_numbers(a, b)

elif player == 6:
    a = float(input('Please enter a number: '))
    b = float(input('Please enter a number: '))

    subtract_numbers(a, b)

elif player == 7:
    a = float(input('Please enter a number: '))
    b = float(input('Please enter a number: '))

    multiply(a, b)

elif player == 8:
    a = float(input('Please enter a number: '))
    b = float(input('Please enter a number: '))

    divide(a, b)

elif player == 9:
    print('Please enter two numbers from 1 to 10. The second number must to be greater than the first!')
    x = float(input('Please enter a number: '))
    y = float(input('Please enter a number:'))

    decimal_to_percent(x, y)

elif player == 10:
    print(time.asctime())
