"""
All the functions you've made so far have had names.

They have started in the form

def some_function(argument1, argument2):
    # some code goes here

In this case,  you have a named function called `some_function`.

But not functions need to have names! You can make functions that are `anonymous`.

You make one using the `lambda` keyword in Python.

Some examples are below.
"""

doubleThat = lambda x: x * 2

# Now, doubleThat is a function that takes in one input, and returns that input * 2.
print(doubleThat(5))
# > 10

splitString = lambda string: string.split()

print(splitString("This is a sentence."))
# > ['This', 'is', 'a', 'sentence.']


add_two = lambda x, y: x + y
print(add_two(50, 100))
# > 150

"""
OK.

You might say, wait, aren't we still naming these functions? What makes them anonymous.

And you're right. The functions `doubleThat` and `splitString` are not anonymous. The fact
that they have names (e.g., `splitString`) means they are not anonymous.

Below are some actual anonymous functions that don't have names.

But first, we will make a regular function.
"""

def apply_anonymous_function(anon_func):
    result = anon_func(10)
    return result

print(apply_anonymous_function(lambda x: x * 2))
# -----------------------------^^^^^^^^^^^^^^^---- that is an anonymous function!
# We call it `anonymous` because it doesn't have any name that we can use to
# refer to it.

"""

The general syntax of an anonymous function:

    lambda argument1, argument2 ... : <some return value here>

For example:

    lambda x, y: x + y

The function above takes in two arguments, x and y, and then returns their sum.

Okay ...

Wait, so what's the point of defining anonymous functions with the `lambda` keyword?

Great question. It's most useful when we want to define short, simple functions that only need
to be defined and used once and we don't want to take up a lot more space (in terms of lines of code).
"""
