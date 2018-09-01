
# ===============
# size2.py
# ===============

# =========================
# Next and Ranges
# =========================

# A Generator works like an iterator
# And we can use "next" to get the next value instead of using it in a loop like in size.py

# We can demonstrate how to use "next" in below code.

# we saw in size.py that my_range starts with 0 when inside the loop
# However when we add "next" in LINE_5, print(next(big_range)), it starts by returning 1 inside the loop
# This is because LINE_5 calls the next function which gets the next value from our generator
# Since we have not used the generator yet, its next value is the first value which is 0

# my_range starts
# my_range is returning 0
# Next is returning = 0  <<====== next returns first value 0
# <class 'generator'>
# big_range (my_range) Memory = 48 bytes
# =====
# Test Line_3 - before loop
# my_range is returning 1  <<======= inside loop starts with 1
# Test Line_4 - Inside loop
# my_range is returning 2

# Also note that the for loop (starting LINE_2) will add all values in generator (0 to 4) if there is no "next"
# If "next" is used, it consumes the first value (0) before the generator enters the for loop
# so the for loop now gets values (1 to 4)

# big_list = [1, 2, 3, 4]      # with next
# big_list = [0, 1, 2, 3, 4]   # without next

# This explains why it is usually a bad idea to assign a generator (my_range) to a variable (big_range)
# See more on this in next section

import sys

big_range = range(10)
print("big_range (range) Memory = {} bytes".format(sys.getsizeof(big_range)))

print("="*5)
big_list = []  # Define an empty list
for val in big_range:
    big_list.append(val)   # This one adds the cumulative sum from 1 to 999 and stores it in big_list
print("big_list Memory = {} bytes".format(sys.getsizeof(big_list)))

print("="*30)

def my_range(n: int):
    print("my_range starts")  # LINE_3. Shows when my_range starts
    start = 0
    while start < n:
        print("my_range is returning {}".format(start))  # LINE_4. This prints the value of start with every iteration
        yield start  # Change to return and will get Error: "TypeError: 'int' object is not iterable"
        start += 1


_=input("Test Line_1")
big_range = my_range(5)   # LINE_1

_=input("Test Line_2")

print("Next is returning = {}".format(next(big_range)))  # LINE_5

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
print("big_range = {}".format(big_range))  # big_range is a generator object based on our function my_range
print("big_list = {}".format(big_list))   # big_list is a list of the values in the range.




# =====================================================================
# Demonstrating why it is not good to assign a generator to a variable
# =====================================================================

# it is usually a bad idea to assign a generator (my_range) to a variable (big_range)
# In this code, we will remove the _=input so program runs without asking us to enter

# When we add another for loop to loop through big_range, (LINE_6), we see it does not produce anything.
# So storing my_range (generator) in big_range (variable) is fine (LINE_1) if you want to call next each time you want a new value
# but its not a good idea if you want to use the variable (big_range) again in a for loop, because there will be nothing there

# if you want to reuse it, you can use the my_range(5) in the loop. LINE_7


import sys

big_range = range(10)
print("big_range (range) Memory = {} bytes".format(sys.getsizeof(big_range)))

print("="*5)
big_list = []  # Define an empty list
for val in big_range:
    big_list.append(val)   # This one adds the cumulative sum from 1 to 999 and stores it in big_list
print("big_list Memory = {} bytes".format(sys.getsizeof(big_list)))

print("="*30)

def my_range(n: int):
    print("my_range starts")  # LINE_3. Shows when my_range starts
    start = 0
    while start < n:
        print("my_range is returning {}".format(start))  # LINE_4. This prints the value of start with every iteration
        yield start  # Change to return and will get Error: "TypeError: 'int' object is not iterable"
        start += 1


# _=input("Test Line_1")

# big_range = range(5)      # LINE_8
big_range = my_range(5)   # LINE_1

# _=input("Test Line_2")

print("Next is returning = {}".format(next(big_range)))  # LINE_5

print(type(big_range))  # use this to find class type when using "yield" or "return"
print("big_range (my_range) Memory = {} bytes".format(sys.getsizeof(big_range)))


print("="*5)
big_list = []  # Define an empty list

# _=input("Test Line_3 - before loop")

for val in big_range:   # LINE_2
    # _=input("Test Line_4 - Inside loop")
    big_list.append(val)   # This one adds the cumulative sum from 1 to 999 and stores it in big_list
print("big_list Memory = {} bytes".format(sys.getsizeof(big_list)))

# We will print the output of big_range and big_list

print("="*30)
print("big_range = {}".format(big_range))  # big_range is a generator object based on our function my_range
print("big_list = {}".format(big_list))   # big_list is a list of the values in the range.

# Now we add another loop to see if there is anything in big_range after last for loop was ran
# We see that this loop is not producing any results

print("="*30)
print("Looping again ... or Not:")  # LINE_6
for i in big_range:
    print("i is {}".format(i))

# Can use generator my_range if you want to use for loop again.

print("="*30)
print("Looping generator my_range:")  # LINE_7
for i in my_range(5):  # Can use my_range (generator) here and it will call my_range 5 times depending on the argument you pass it
    print("i is {}".format(i))




# ======================================
# Using Range
# ======================================

# NOTE that you can store range(x) to a variable and it will work.
# LINE_8 is storing range(5) to variable big_range
# We need to remove "next" in LINE_5 otherwise it will give error: TypeError: 'range' object is not an iterator
# When you run this code, you can loop variable big_range as many times as you like.
# This is because the range(x) class is reset every time it is used, unlike our function my_range

import sys

big_range = range(10)
print("big_range (range) Memory = {} bytes".format(sys.getsizeof(big_range)))

print("="*5)
big_list = []  # Define an empty list
for val in big_range:
    big_list.append(val)   # This one adds the cumulative sum from 1 to 999 and stores it in big_list
print("big_list Memory = {} bytes".format(sys.getsizeof(big_list)))

print("="*30)

def my_range(n: int):
    print("my_range starts")  # LINE_3. Shows when my_range starts
    start = 0
    while start < n:
        print("my_range is returning {}".format(start))  # LINE_4. This prints the value of start with every iteration
        yield start  # Change to return and will get Error: "TypeError: 'int' object is not iterable"
        start += 1


# _=input("Test Line_1")

big_range = range(5)      # LINE_8
# big_range = my_range(5)   # LINE_1

# _=input("Test Line_2")

# print("Next is returning = {}".format(next(big_range)))  # LINE_5

print(type(big_range))  # use this to find class type when using "yield" or "return"
print("big_range (my_range) Memory = {} bytes".format(sys.getsizeof(big_range)))


print("="*5)
big_list = []  # Define an empty list

# _=input("Test Line_3 - before loop")

for val in big_range:   # LINE_2
    # _=input("Test Line_4 - Inside loop")
    big_list.append(val)   # This one adds the cumulative sum from 1 to 999 and stores it in big_list
print("big_list Memory = {} bytes".format(sys.getsizeof(big_list)))

# We will print the output of big_range and big_list

print("="*30)
print("big_range = {}".format(big_range))  # big_range is a generator object based on our function my_range
print("big_list = {}".format(big_list))   # big_list is a list of the values in the range.

# Now we add another loop to see if there is anything in big_range after last for loop was ran
# We see that this loop is not producing any results

print("="*30)
print("Looping again ... or Not:")  # LINE_6
for i in big_range:
    print("i is {}".format(i))

# Can use generator my_range if you want to use for loop again.

print("="*30)
print("Looping generator my_range:")  # LINE_7
for i in my_range(5):  # Can use my_range (generator) here and it will call my_range 5 times depending on the argument you pass it
    print("i is {}".format(i))


