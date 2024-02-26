# Verkefni 1
def power(num, pos_int):
    return num**pos_int
'''Tímaflækja = O(1)'''

# Verkefni 2
def multi_int(num1, num2):
    
    num_sum = 0
    for _ in range(num2):
        num_sum += num1

    return num_sum
'''Tímaflækja = O(n)'''

# Verkefni 3
import random
def random_replacement(lis):
    for i in range(len(lis)):
        lis[i] = random.randint(1, 6)
    return lis
'''Tímaflækja = O(n)'''

# Verkefni 4
def display_list(lis):
    for i in lis:
        if lis[len(lis)-1] == i:
            print(i)
        else:
            print(i, end=", ")
'''Tímaflækja = O(n)'''

# Verkefni 5
def random_list_jump(lis):

    check_list = []

    while len(check_list) < len(lis):
        ran_num = random.randint(1, len(lis))
        if ran_num not in check_list:
            check_list.append(ran_num)
        lis[ran_num-1] += 1

    return lis
'''Tímaflækja O(n**2)'''

# Verkefni 6
def create_and_switch():
    rand_size = random.randint(1, 10)
    a_list = []
    for i in range(rand_size):
        rand_num = random.randint(1, 10)
        a_list.append(rand_num)

    print(a_list)

    switcher = a_list[1]
    a_list[1] = a_list[2]
    a_list[2] = switcher

    print(a_list)

    rand_switch = random.randint(1, len(a_list))
    if rand_switch < len(a_list):
        switcher = a_list[rand_switch+1]
        a_list[rand_switch] = switcher
        a_list[rand_switch+1] = a_list[rand_switch]
    else:
        switcher = a_list[rand_switch-1]
        a_list[rand_switch] = switcher
        a_list[rand_switch-1] = a_list[rand_switch]

    print(a_list)

create_and_switch()