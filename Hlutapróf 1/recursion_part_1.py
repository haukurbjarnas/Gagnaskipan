def power(base, exp):

    if exp == 1:
        return base
    
    else:
        return base * power(base, exp-1)



def multiply(a, b):
    
    if b == 1:
        return a
    
    else:
        return a + multiply(a, b-1)
    


def factiorial(n):

    if n == 1:
        return n
    
    else:
        return n * factiorial(n-1)
    

# Virkar ekki
def natural(n):

    if n == 1:
        print(n)
    
    else:
        return f'{n}, {natural-1}'






def sum_of_digits(x):

    if x < 10:
        return x
    
    else:
        return x % 10 + sum_of_digits(x//10)


