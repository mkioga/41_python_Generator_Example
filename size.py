
# ===========
# size.py
# ===========

# ====================================================
# Generators, Comprehensions and Lambda Expressions
# ====================================================

# These are more advanced python features.
# Generators - used to work with huge amounts of data
# Comprehensions - Can let us to things that would be difficult with standard iterators
# Lambdas - We will see what they are, why python has them, and alternatives to using them


# =============================
# Generators and Yield
# =============================

# we are going to look at python generators and generator functions.

# Since one of the advantages of generators is they save memory, we will first learn how to
# check how much memory things use in python


# =================
# size.py
# =================

# fist we import sys

import sys


big_range = range(10)  # Here we start with range 10. can increase to 100, 1000 etc to check memory differences
print("big_range = {}".format(big_range))  # shows that range is: range(0, 10)

# This prints out what is in that range.
print("big_range (list) = ", end='')
for x in big_range:  # prints what is in the range
    print(x, end=',')
print()


# Then we get the Memory size in bytes that big_range occupies
# This is the size before we add some data in it.

print("big_range Memory = {} bytes".format(sys.getsizeof(big_range)))

# We create a list (big_list) containing all the values in big_range i.e. cumulative sum from 1 to 999

big_list = []  # Define an empty list

for val in big_range:
    big_list.append(val)   # This one adds the cumulative sum from 1 to 999 and stores it in big_list

# Print the big_list

print("big_list (list) = {}".format(big_list))

# print Memory size of big_list in bytes (i.e. bytes occupied by big_list

print("big_list Memory = {} bytes".format(sys.getsizeof(big_list)))

# when we run this code, we get result:

# big_range = range(0, 1000)
# big_range uses = 24 bytes
# big_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, <<== truncate ==> 994, 995, 996, 997, 998, 999]
# big_list uses = 4516 bytes
#



# ===================================================================
# we will use below shorter version of above code without comments
# ====================================================================

# you will notice that when using big_range, which is from function "range(1000), it uses 24 bytes
# even if you increase if from 10, to 1,000, to 10,000 to 100,000 etc

# but when you manually add the range and put it in big_list , the bytes used increases
# exponentially from 100 to 460 to 4516 to 43,816, to 412,236 bytes when you increase range from
# 10 to 100 to 1000 to 10000 etc

# So we can see there is a huge difference in memory used by the two objects (big_range, and big_list)
# when they are actually storing the same amount of data i.e. data in the range specified.

# Both big_range and big_list are iterators and you can use either of them in a for loop to iterate all their values.

# BUT big_range is a special case of an iterator called a "Generator"

# NOTE: we will shorten code below and only print the memory so we can compare memory.
# So if you understand how this code works, move to next code displaying memory only



import sys

big_range = range(10)
print("big_range (range) = {}".format(big_range))  # shows that range is: range(0, 10 or 1000 or whatever you put)

# This prints out what is in that range.
print("big_range (list) = ", end='')
for x in big_range:
    print(x, end=',')
print()

print("big_range (range) Memory = {} bytes".format(sys.getsizeof(big_range)))

print("="*10)
big_list = []  # Define an empty list
for val in big_range:
    big_list.append(val)   # This one adds the cumulative sum from 1 to 999 and stores it in big_list
print("big_list Memory = {} bytes".format(sys.getsizeof(big_list)))

print("="*20)

# ==================================

# We can create our own "range" function and call it "my_range"
# Our function named "my_range" that acts like inbuilt function "range"

def my_range(n: int):
    start = 0
    while start < n:
        yield start
        start += 1

# we call our function "my_range" and pass it range parameter n = 10
# Then assign the result to variable "big_range"

big_range = my_range(10)

# When you print this line, it gives:
# big_range (my_range) = <generator object my_range at 0x008FDED0>
# This means that big_range is a generator object based on my_range function

print("big_range (my_range) = {}".format(big_range))  # shows that range is: range(0, 10 or 1000 or whatever you put)

# This prints out what is in that range.
print("big_range (my_range) list = ", end='')
for x in big_range:
    print(x, end=',')
print()

print("big_range (my_range) Memory = {} bytes".format(sys.getsizeof(big_range)))


print("="*10)
big_list = []  # Define an empty list
for val in big_range:
    big_list.append(val)   # This one adds the cumulative sum from 1 to 999 and stores it in big_list

print("big_list Memory = {} bytes".format(sys.getsizeof(big_list)))






# ==============================
# Code displaying memory only:
# ==============================
# NOTE: range = builtin range and my_range is our own range function

# Here we see the following results
# Passed range : range Memory :  my_range Memory : big_list Memory
# 10           : 24           : 48               : 100
# 100          : 24           : 48               : 460
# 1000         : 24           : 48               : 4516
# 10000        : 24           : 48               : 43816


# We can see from above result that using inbuilt range function uses 24 and using our function my_range uses 48
# Both of these are using very small memory compared to big_list list we used to add all the contents of the range.


import sys

big_range = range(10000)
print("big_range (range) Memory = {} bytes".format(sys.getsizeof(big_range)))

print("="*5)
big_list = []  # Define an empty list
for val in big_range:
    big_list.append(val)   # This one adds the cumulative sum from 1 to 999 and stores it in big_list
print("big_list Memory = {} bytes".format(sys.getsizeof(big_list)))

print("="*30)

# ==================================

# We can create our own "range" function and call it "my_range"
# Our function named "my_range" that acts like inbuilt function "range"

def my_range(n: int):
    start = 0
    while start < n:
        yield start
        start += 1

# we call our function "my_range" and pass it range parameter n = 10
# Then assign the result to variable "big_range"

big_range = my_range(10000)

print("big_range (my_range) Memory = {} bytes".format(sys.getsizeof(big_range)))


print("="*5)
big_list = []  # Define an empty list
for val in big_range:
    big_list.append(val)   # This one adds the cumulative sum from 1 to 999 and stores it in big_list
print("big_list Memory = {} bytes".format(sys.getsizeof(big_list)))




# ==============================
# Code displaying memory only:
# ==============================


import sys

big_range = range(10)
print("big_range (range) Memory = {} bytes".format(sys.getsizeof(big_range)))

print("="*5)
big_list = []  # Define an empty list
for val in big_range:
    big_list.append(val)   # This one adds the cumulative sum from 1 to 999 and stores it in big_list
print("big_list Memory = {} bytes".format(sys.getsizeof(big_list)))

print("="*30)

# ==================================

# We can create our own "range" function and call it "my_range"
# Our function named "my_range" that acts like inbuilt function "range"

# So what is my_range function doing and why does it have "yield" statement instead of "return" statement ?

# When you write a normal function, the function finishes after returning the result.

# With "yield" it returns my_range as <class 'generator'> and uses 48 bytes
# if you replace "yield" with "return", you get error: "TypeError: 'int' object is not iterable" and uses 12 bytes
# The differences in memory used shows that the returned objects are different.

# There is error because we cannot iterate over an integer
# my_range with "return" returns a single value (class int) and then stops as opposed to what it was returning before i.e <class 'generator'>.
# NOTE: find type with print(type(big_range))

# When using "yield", the function returns the yielded value and then goes into a suspended state
# it also keeps track of all its variables. And the next time its called, it wakes up and continues from where it left off.

# big_range value in LINE_1 is called every time its iterated on the loop in LINE_2
# We can confirm this on LINE_4 which shows it incrementing by the range passed to it in LINE_1 and used in LINE_2

# To see how the program executes step by step, we add "_=input("Test Line_x")
# to require us to hit "Enter" before it moves to next line.


def my_range(n: int):
    print("my_range starts")  # LINE_3. Shows when my_range starts
    start = 0
    while start < n:
        print("my_range is returning {}".format(start))  # LINE_4. This prints the value of start with every iteration
        yield start  # Change to return and will get Error: "TypeError: 'int' object is not iterable"
        start += 1


# we call our function "my_range" and pass it range parameter n = 10
# Then assign the result to variable "big_range"

_=input("Test Line_1")
big_range = my_range(5)   # LINE_1

_=input("Test Line_2")

# print(next(big_range))   # LINE_5
print(type(big_range))  # use this to find class type when using "yield" or "return"
print("big_range (my_range) Memory = {} bytes".format(sys.getsizeof(big_range)))


print("="*5)
big_list = []  # Define an empty list

_=input("Test Line_3 - before loop")

for val in big_range:   # LINE_2
    _=input("Test Line_4 - Inside loop")
    big_list.append(val)   # This one adds the cumulative sum from 1 to 999 and stores it in big_list
print("big_list Memory = {} bytes".format(sys.getsizeof(big_list)))

# ============================

print("="*30)
print(big_range)  # big_range is a generator object based on our function my_range
print(big_list)   # big_list is a list of the values in the range.


# When you run code above, you will get this result:
# The "generator" function my_range, assigned to variable "big_range" is called by loop on LINE_2
# Which extracts its contents

# Test Line_1
# Test Line_2
# <class 'generator'>
# big_range (# my_range) Memory = 48 bytes
# =====
# Test Line_3 - before loop
# my_range starts
# my_range is returning 0  <===== starts with 0
# Test Line_4 - Inside loop
# my_range is returning 1
# Test Line_4 - Inside loop
# my_range is returning 2
# Test Line_4 - Inside loop
# my_range is returning 3
# Test Line_4 - Inside loop
# my_range is returning 4
# Test Line_4 - Inside loop
# big_list Memory = 68 bytes
# ==============================
# <generator object # my_range at 0x02F4DED0>
# [0, 1, 2, 3, 4]

