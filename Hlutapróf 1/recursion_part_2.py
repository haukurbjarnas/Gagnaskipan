def len_of_str(a_str):

    if len(str(a_str)) == 1:
        return 1
    
    else:
        return 1 + len_of_str(a_str[1:])
    

def linear_search(lis, val):

    if len(lis) > 0:
        if lis[0] == val:
            return True
        
    if len(lis) == 0:
        return False
    
    else:
        return linear_search(lis[1:], val)
    

def count_instances(lis, val):

    if len(lis) > 0:
        if lis[0] == val:
            return 1 + count_instances(lis[1:], val)
        
    if len(lis) == 0:
        return 0
    
    else:
        return count_instances(lis[1:], val)
    


