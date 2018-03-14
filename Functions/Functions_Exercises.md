# Function Exercises
By Carl Shan of [The Nueva School](www.nuevaschool.org)

Below are some exercises to work on as you learn about functions:

## Introductory:

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


2. Create your own function that takes in 2 inputs and returns the remainder when the first input is divided by the second.


> **HINT:** Look up the modulus operator in Python: %

## Intermediate:

1. Create a function that takes a piece of text as an input, and prints its reverse.
> **HINT:** You will have to look up how to reverse a piece of text.

2. Create a function that allows you to move your turtle around.
> **HINT**: You’ll have to use the `onkey` function which is from the turtle module: link.
> To use the `onkey` function, make sure you have a line of code in your file that is:
>
> `from turtle import onkey`


## Advanced:
1. Solve the following problem (from [Project Euler](www.projecteuler.net)): 

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

2. Solve the following problem (from [Project Euler](www.projecteuler.net)): 

```
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Write a function that returns the largest palindrome made from the product of two 3-digit numbers.
```


