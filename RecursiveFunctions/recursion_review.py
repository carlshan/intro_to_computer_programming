# In order to understand recursion, one must first understand recursion.
# They took me years to understand, so don't worry if you don't
# get it right now.
# Recursion is about finding a way of solving a problem
# by breaking it down into its simplest solution
# and then building up to solve the big problem.

# We may want to solve a problem recursively because it's
# easier to write and debug, since the code is often shorter
# than if we wrote it iteratively (e.g., with a loop and many variables)


# There are two key parts to a recursive function:
# 1. The Base Case (AKA the Terminating Condition)
# This is usually the "simplest case" that we are interested in
# and is when the function "ends" or no longer recurses.
# 2. The Recursive Case
# This is why the function we are defining CALLS ITSELF, which is called
# recursion.

# Let's break this down by looking at some problems and see if we can find
# the base case, recursive case

# Factorial
# Fibonacci
# Sum
# Challenge: Flatten a list

[5, [1, 2]]

def flatten(mylist):
    # base case
    if mylist == []:
        return []
    elif type(mylist[0]) == int:
        return [mylist[0]] + flatten(mylist[1:])
    elif type(mylist[0]) == list:
        return flatten(mylist[0]) + flatten(mylist[1:])



















def flatten(lst):
    if lst == []: # base case
        return lst
    elif type(lst[0]) == int:
        return [lst[0]] + flatten(lst[1:])
    elif type(lst[0]) ==  list: # recursive case
        return flatten(lst[0]) + flatten(lst[1:])

test = [1, [2, 3, [4, 5, 6]]]
# expected = [1, 2, 3, 4, 5, 6]
print(flatten(test))

        # do something

def sum_recursive(l):
    if l == []:
        return 0
    else:
        return l[0] + sum_recursive(l[1:])
