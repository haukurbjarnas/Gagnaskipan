def length_of_string(string):

    if string == '':
        return 0
    else:
        return 1 + length_of_string(string[1:])
    
def linear_search(lis, n):

    if not lis:
        return False
    else:
        if lis[0] == n:
            return True
        else:
            return linear_search(lis[1:], n)

def count_instances(lis, n):

    if not lis:

        return False
    
    else:

        if lis[0] == n:
            return 1 + count_instances(lis[1:], n)
        else:
            return 0 + count_instances(lis[1:], n)
        
def duplicates(lis):

    if not lis:
        return False
    
    else:

        if lis[0] in lis[1:]:
            return True
        else:
            return duplicates(lis[1:])