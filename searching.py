import random
import timeit


lst = sorted([random.randint(0, 1000000) for _ in range(1000000)])

to_find = random.randint(0, 10)

def linear_search(lst, to_find):

    for x in lst:
        if x == to_find:
            return True

    return False

# print(lst)
# print(to_find)
print(linear_search(lst, to_find))