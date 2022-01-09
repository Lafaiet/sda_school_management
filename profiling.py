import timeit
import time

setup = '''
import random
'''


linear_search_code = '''
    
lst = sorted([random.randint(0, 10000000) for _ in range(10000000)])

to_find = random.randint(0, 10)

found = False

for x in lst:
        if x == to_find:
            found = True
            break
            
print(found)
    
'''

start = time.time()
print(timeit.repeat(stmt=linear_search_code, setup=setup,number=1, repeat=5))
end = time.time()

print(end-start)

