
# ====================
# scratchpad.py
# ====================

# ==================================
# More uses for Generators
# ==================================

# First we are going to see python behavior or evaluating numbers on the right first

# ===================
# Swapping values
# ===================

# Original numbers

a = 2
b = 3

print("a = {}, b = {}".format(a, b))

# These numbers are able to be swapped because python evaluates from right to left
# so original a (2) is assigned to b, and original b (3) is assigned to a

a, b = b, a

print("a = {}, b = {}".format(a, b))

# In other languages, you would need to introduce a temporary variable to hold the numbers

temp = a
a = b
b = temp

print("a = {}, b = {}".format(a, b))

















