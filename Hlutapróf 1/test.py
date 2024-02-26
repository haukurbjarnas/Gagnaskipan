def remove_odd_indexes(lis, counter=0):

    if counter == len(lis):
        return lis
    
    if counter % 2 == 0:
        counter += 1
        return remove_odd_indexes(lis, counter)

    else:
        lis.remove(lis[counter])
        counter += 1
        return remove_odd_indexes(lis, counter)


lis = [1, 2, 3, 4, 5]

print(remove_odd_indexes(lis))