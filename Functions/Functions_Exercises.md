# Function Exercises
By Carl Shan of [The Nueva School](www.nuevaschool.org)

Below are some exercises to work on as you learn about functions.

Make a new Python `.py` file to do all of these exercises.

## Introductory: Do these first

1. What do you think running the following command will do?

Consider this function:

```python
def what_does_this_do(a, b, c, d):
    if a > b:
        return c + d
    else:
        return (a * b * c) / (d + 2)

```

Now, what should the function call below produce?

`what_does_this_do(5, 10, 15, 20)`

What about this call to the function?

`what_does_this_do(10, 5, 15, 20)`

Put your answers as comments (using the `#` symbol in Python) in your code file.

2. Create your own function named `remainder` that takes in 2 numbers as inputs and returns the remainder when the first input is divided by the second.

> **HINT:** Look up the modulus operator in Python: `%`

Example:

```python
print(remainder(10, 2))
# the above should print
# 0

print(remainder(9, 2))
# the above should print
# 1

```

3. Write a function called `is_between` that takes three numbers as inputs, and returns whether the first number is in between the last two. This function should return `True` if the first number is in between, and `False` otherwise.

Example:

```python
print(is_between(5, 1, 110))
# the above should print
# True

print(is_between(5, 50, 100))
# the above should print
# False
```

## Intermediate:

1. Create a function named `reverse` that takes a piece of text as an input, and prints its reverse.
> **HINT:** You will have to look up how to reverse a piece of text.

```python
print(reverse("Carl"))
# the above should print
# 'larC'
```

2. Write a function named `factorial` that takes a number as input and returns the factorial of that number. This function should return the special Python value of `None` if the input number is a negative one, since you cannot take the factorial of a negative number.

> **HINT**: Remember, the factorial of a number `n` is equal to `n * (n-1) * (n-2) * ... * 2 * 1`.

Example:

```python
print(factorial(5))
# running the above code should return
# 120

print(factorial(-100))
# running the above line of code should return
# None
```

3. Create a function named `count_unique` that accepts a list as input, and returns a new list containing only the unique elements of the first list.

Example:

```python
elements = [1, 2, 2, 2, 3, 4, 99, 5, 5, 99]

unique = count_unique(elements)

print(unique)
# the above should print the below in some order
# [1, 2, 3, 4, 99, 5]
```

> **HINT**: Look up how the `in` operator works in in Python. Think about how you can use that.

## Advanced:
1. Solve the following problem (from [Project Euler](https://projecteuler.net/)): 

```
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Write a function that returns the sum of all the multiples of 3 or 5 below 1000.
```

> **HINT:** You may want to use the modulus operator.
> 
> **HINT:** The ‘%’ operator is like the ‘+’ operator in python. You can put it between two numbers. Except the ‘%’ operator is known as the modulus opertor. It returns the remainder when the first number is divided by the second.
> 
> For example,  the Python expression `10 % 5` will return 0.
> 
However, `10 % 4` will return 2, since there is a remainder of 2 when 10 is divided by 4.
> 

2. Solve the following problem (from [Project Euler](https://projecteuler.net/)): 

```
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Write a function that returns the largest palindrome made from the product of two 3-digit numbers.
```

3. One of the most important properties of numbers is whether they are prime. This is because prime numbers are the building blocks of all other numbers (see [Fundamental theorem of arithmetic](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic)). So it is really important to know whether a number is prime.

Write a function called `is_prime` that takes a number as an input and returns `True` if the number is prime and `False` otherwise.


4. Write a function called `binarize` that takes a single number as input, and returns a string of text that is the binary representation of that number (e.g., 010011). If you do not know how binary representation works, you can watch this short [3 minute video](https://www.youtube.com/watch?v=H4BstqvgBow).

> **NOTE**: This is a pretty challenging problem. You may want to do this with a classmate.

> **HINT**: If you are having trouble, write out a step-by-step list of instructions in plain English as to how you might want to begin. Then translate the easier steps into Python.

> **HINT**: Try to solve a simpler version of the problem first. Doing so will give you a large hint as to how to solve the full problem. Simplify it by giving the problem some constraints. What if you knew, for example, that the number that you are attemping to `binarize` is a power of 2? What if you knew that it was an odd number? How would you write the function in these situations?

Example:

```python
print(binarize(5))
# the above should print
# 101

print(binarize(10))
# the above should print
# 1010

```

5. Write a program where users can play tic-tac-toe against each other. 

> **HINT**: You will likely need to use the `raw_input()` function. You will also need to run your code in Terminal to allow for user input, since Atom won't allow you to easily enter in input.