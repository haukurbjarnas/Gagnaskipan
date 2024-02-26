import math

# O(1)
def o_1 (num1, num2):
    if num1 > num2:
        print(num1)
    else:
        print(num2)

# O(log2n)

# O(n)
def o_n(num):
    counter = 1
    for _ in range(num):
        if math.factorial(_) > 10:
            print(counter)
        counter += 1

o_n(7)

# O(n*log2n)

# O(n**2)

# O(n**3)

# O(2**n)
        
