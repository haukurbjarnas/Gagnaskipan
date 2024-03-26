def power(base, exp):

    if exp == 0:
        return 1

    else:
        return base * power(base, exp-1)

def multiply(a, b):

    if a == 0 or b == 0:
        return 0
    else:
        return a + multiply(a, b-1)
    

def factorial(a):
    if a == 0:
        return 0
    if a == 1:
        return 1
    else:
        return a * factorial(a-1)
    

def natural(a):

    if a > 0:
        natural(a-1)
        print(a, end=' ')


def sum_of_digits(x):
    
    if x == 0:
        return 0
    
    return (x%10) + sum_of_digits(x//10)


def fibonacci_1(x):

    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci_1(x-1) + fibonacci_1(x-2)
    
def fibonacci(x):

    if x == 0: return 0
    elif x == 1: return 1
    