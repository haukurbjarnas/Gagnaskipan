import random

# Time complexity: O(1)
def power(integer, exp):

    return integer**exp


# Time complexity: O(n)
def multiply(int1, int2):

    sum = 0

    for _ in range(int2):

        sum += int1

    return sum


# Time complexity: O(n)
def random_list(size):

    lis = [0]*size

    for i in range(len(lis)):

        rand_int = random.randint(1, 6)

        lis[i] = rand_int


    return lis


# Time complexity: O(n)
def print_list(lis):

    for i in range(len(lis)):

        if i == len(lis)-1:

            print(lis[i])

        else:
            print(f'{lis[i]}', end=', ')


# Time complexity: O(n**2)
def increase_random_index(lis):

    check_lis = []


    while len(check_lis) < len(lis):
        rand_ind = random.randint(0, len(lis)-1)

        lis[rand_ind] += 1

        if rand_ind in check_lis:
            pass
        else:
            check_lis.append(rand_ind)

    return lis


# Time complexity: O(n)
def list_switcher(size, index):

    lis = []

    for i in range(size):

        rand_var = random.randint(0, 100)

        lis.append(rand_var)

    new_var = lis[index+1]

    lis[index+1] = lis[index]
    lis[index] = new_var

    rand_index = random.randint(0, size-1)

    random_var = lis[rand_index+1]

    lis[rand_index+1] = lis[rand_index]
    lis[rand_index] = random_var

    return lis


def randomly_ordered_list():

    lis = []

    while len(lis) < 6:

        rand_int = random.randint(1, 6)

        if rand_int in lis:
            pass
        else:
            lis[rand_int-1] = rand_int

    return lis

print(randomly_ordered_list())