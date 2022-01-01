# 1) Iterate With enumerate() instead of range(len())

data = [1, 2 , -4, -3]
for i in range(len(data)):
    if data[i] < 0:
        data[i] = 0

print(data)

for idx, num in enumerate(data):
    print(idx, num)
    if num < 0:
        data[idx] = 0

print(data)

# 2) Use List Comprehensions Instead of for raw loops

square = []
for i in range(10):
    square.append(i*i)

print(square)

square = [i*i for i in range(10)]
print(square)

# 3) Sort complex iterable with sorted()

data = (3, 5, 1, 10, 9)
sorted_data = sorted(data, reverse=True)

print(sorted_data)

data = [{"name": "Max", "age": 6},
        {"name": "Lisa", "age": 20},
        {"name": "Ben", "age": 9}]

sorted_data = sorted(data, key=lambda x:["age"])
print(sorted_data)

# 4) Store unique values with Sets

my_list = [1,2,3,4,5,6,7,7,7]
my_set = set(my_list)
print(my_set)

primes = {2,3,5,7,11,13,17,19}
print(primes)

# 5) Save Memory with Generators
import sys

my_list = [i for i in range(10000)]
print(sum(my_list))
print(sys.getsizeof(my_list), "bytes")

my_gen = (i for i in range(10000))
print(sum(my_gen))
print(sys.getsizeof(my_gen), "bytes")

# 6) Define default values in Dictionaries with .get() and .setdefault()

my_dict = {"item": "football", "price": 10.00}
count = my_dict.get("count", 0)

count = my_dict.setdefault("count", 0)
print(count)
print(my_dict)

# 7) Count hashable objects with collections.Counter
from collections import Counter

my_list = [10,10,10,5,5,2,9,9,9,9,9,9]
counter = Counter(my_list)

most_common = counter.most_common(1) # 두번째는 2 (튜플 형식)
print(most_common[0])

# 8) Format strings with f-Strings

name = "Alex"
my_string = f"Hello {name}"
print(my_string)

i = 10
print(f"{i} squared is {i*i}")

# 9) concat string with .join()

list_of_strings = ["Hello", "my", "friend"]

my_string = " ".join(list_of_strings)
print(my_string)

# 10) merge two dictionaries

d1 = {"name": "Alex", "age": 25}
d2 = {"name": "Alex", "city": "New York"}
# merged_dict = {**d1, **d2}
merged_dict = d1 | d2
print(merged_dict)

# 11) simplify if statement for multiple checks

colors = ["red", "green", "blue"]

c = "red"
if c in colors:
    print(f"{c} is main color")