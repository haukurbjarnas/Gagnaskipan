def modulus(a, b):  # ONLY NEEDS TO WORK FOR POSITIVE INTEGERS
    #TODO: remove 'pass' and implement functionality
    
    if a < 0:
        return a+b
    else:
        a -= b
        return modulus(a, b)


print(128%15)