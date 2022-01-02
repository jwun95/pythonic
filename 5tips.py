# 1. pdb

import pdb
pdb.set_trace() # n

# 2. virtual env

# 3. list, dictionary
fruits = [
    {'name': 'apple', 'price': 20},
    {'name': 'avocado', 'price': 10},
    {'name': 'orange', 'price': 5},
]

print(
    [fruit['name'] for fruit in fruits],
    {fruit['name']: fruit['price'] for fruit in fruits}
)

# 4. lambda
def add(x, y):
    return x + y

add2 = lambda x,y: x+y

# 5. lambda 2

nums = [1,2,3]

def is_greater_than_one(x):
    return x > 1

more_than_one_nums = filter(is_greater_than_one, nums)
more_than_one_nums = filter(lambda x: x > 1, nums)
