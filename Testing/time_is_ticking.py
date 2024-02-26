from time import time

start_time = time()

num = 100
for _ in range(num):
    print(num)
    num -= 1

end_time = time()

elapsed_time = end_time - start_time

print(round(elapsed_time, 5))