
# ==================
# fibonacci.py
# ==================

# =================================================
# Generator uses - Calculating Fibonacci Numbers
# =================================================

# https://en.wikipedia.org/wiki/Fibonacci_number

# Fibonacci numbers are the numbers in the following integer sequence, called the Fibonacci sequence,
# and characterized by the fact that every number after the first two is the sum of the two preceding ones:

# Sometimes it starts with 1;
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, etc

# Often, especially in modern usage, the sequence starts with 0:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, etc

# NOTE: This code has stops ( _=input() ) so you can understand the STEPS it follows
# Go to next code which runs without the stops



def fibonacci():
    # current = 0  # you can initialize normally
    # previous = 1
    current, previous = 0, 1   # or initialize like this

    _=input("Enter to print initial Current and Previous")   # STEP_3: We now enter to print initial current and previous
    print("Initial Current and Previous = {}, {}".format(current, previous))

    while True:
        current, previous = current + previous, current
        _=input("Enter to print New Current and Previous")   # STEP_4: We print new Current and previous
        print("New Current and Previous = {}, {}".format(current, previous))
        yield current  # STEP_5: fibonacci Function will yield New Current and pass it to fib, which prints it

# STEP_1: We call fibonacci function and assign it to variable fib
_=input("Enter to Call fibonacci function")
fib = fibonacci()   # call fibonacci function above and assign it to fib

# STEP_2: We go to first print(next(fib)). NOTE: all prints will be run and we will not return to STEP_2 until they are done
_=input("Enter to Print next(fib):")  # STEP_2: We go to first print(next(fib)).

# STEP_6: Prints the fibonacci number for the iteration in While loop in fibonacci function
# NOTE: print(next) is like a loop. While loop in fibonacci function is True until all these print(next(fib)) are completed

print("next(fib) = New Current = Fibonacci = {}".format(next(fib)))
print("next(fib) = New Current = Fibonacci = {}".format(next(fib)))
print("next(fib) = New Current = Fibonacci = {}".format(next(fib)))
print("next(fib) = New Current = Fibonacci = {}".format(next(fib)))


# =================================================
# Fibonacci code without stops (it starts with 1)
# =================================================
# infinite Generator
# =====================

def fibonacci():
    current, previous = 0, 1   # or initialize like this
    print("Initial Current and Previous = {}, {}".format(current, previous))
    while True:
        current, previous = current + previous, current
        print("New Current and Previous = {}, {}".format(current, previous))
        yield current  # STEP_5: fibonacci Function will yield New Current and pass it to fib, which prints it

# STEP_1: We call fibonacci function and assign it to variable fib
fib = fibonacci()   # call fibonacci function above and assign it to fib

print("next(fib) = New Current = Fibonacci = {}".format(next(fib)))
print("next(fib) = New Current = Fibonacci = {}".format(next(fib)))
print("next(fib) = New Current = Fibonacci = {}".format(next(fib)))
print("next(fib) = New Current = Fibonacci = {}".format(next(fib)))
print("next(fib) = New Current = Fibonacci = {}".format(next(fib)))
print("next(fib) = New Current = Fibonacci = {}".format(next(fib)))
print("next(fib) = New Current = Fibonacci = {}".format(next(fib)))
print("next(fib) = New Current = Fibonacci = {}".format(next(fib)))
print("next(fib) = New Current = Fibonacci = {}".format(next(fib)))
print("next(fib) = New Current = Fibonacci = {}".format(next(fib)))
print("next(fib) = New Current = Fibonacci = {}".format(next(fib)))
print("next(fib) = New Current = Fibonacci = {}".format(next(fib)))


print("="*30)



# =================================================
# Fibonacci code without stops (it starts with 0)
# =================================================
# infinite generator
# ====================

# If you want your fibonacci to start with 0, you put line for yield (STP_2) before you assign New current and New previous

# So def fibonacci() is a GENERATOR that returns successive fibonacci numbers each time we call "next" to get the next value.
# NOTE that this is an INFINITE GENERATOR, which means it will keep generating the next number in the sequence
# And that is why we are using print(next(fib)) rather than trying to loop through the values.

# if for example you use a for loop to run through veriable fib, you will get an infinite loop without a stop

def fibonacci():
    current, previous = 0, 1   # or initialize like this
    print("Initial Current and Previous = {}, {}".format(current, previous))
    while True:
        yield current  # STEP_5: will yield initial current which is 0
        current, previous = current + previous, current
        print("New Current and Previous = {}, {}".format(current, previous))


# STEP_1: We call fibonacci function and assign it to variable fib
fib = fibonacci()   # call fibonacci function above and assign it to fib

print("next(fib) = New Current = Fibonacci = {}".format(next(fib)))
print("next(fib) = New Current = Fibonacci = {}".format(next(fib)))
print("next(fib) = New Current = Fibonacci = {}".format(next(fib)))
print("next(fib) = New Current = Fibonacci = {}".format(next(fib)))
print("next(fib) = New Current = Fibonacci = {}".format(next(fib)))
print("next(fib) = New Current = Fibonacci = {}".format(next(fib)))
print("next(fib) = New Current = Fibonacci = {}".format(next(fib)))
print("next(fib) = New Current = Fibonacci = {}".format(next(fib)))
print("next(fib) = New Current = Fibonacci = {}".format(next(fib)))
print("next(fib) = New Current = Fibonacci = {}".format(next(fib)))
print("next(fib) = New Current = Fibonacci = {}".format(next(fib)))
print("next(fib) = New Current = Fibonacci = {}".format(next(fib)))


# You don't want to print fib using for loop
# This will run an infinite loop because the infinite generator has no stop
# it would continue running intil the number is so large that it uses all the memory in the computer

# for f in fib:
#     print(f)

