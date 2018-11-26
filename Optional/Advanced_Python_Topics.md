# Advanced Programming with Python 
By Carl Shan

## Introduction

Here are a few advanced programming topics in Python and exercises associated with them.    
 
## Topic 1: List Comprehensions 

List compehensions are a way to combine a for-loop and making a list at the same time.

Follow the link to learn about [List Comprehension Expressions](https://www.programiz.com/python-programming/list-comprehension). 

### Exercises
Visit the [Lists Exercises](https://github.com/carlshan/intro_to_computer_programming/blob/master/Lists/List_Exercises.md) link and solve Intermediate #2, Advanced #1 and Advanced #2 using a list comprehension.

## Topic 2: Exception Handling with `try` and `except`

No one likes getting bugs in their code. I'm sure you all haven't either.

However there are two broad types of errors:

1. Syntax Errors: These are errors where you just didn't type something correctly. For example: `print( x + 1` will error because there is no close `)`.
2. Exceptions: This is when syntactically **correct** code produces some error. 

In some situations you may not want your program to quit if it runs into an Exception.

Instead you may want it to handle the Exception a special way that you define (e.g., maybe you want it to continue, and just print the Exception).

You can prevent this from happening by using a `try-except` block.

You use the `try-except` block in the following way:

```python
try:
    # some code here
except:
    # What should happen if your code errors
else:
    # what should happen if your code DOESN'T error

```

Here's an example:

```python
try:
    print(0 / 0)   # <------ You can't divide by 0! So this should error.
except Exception as err: 
    print("Error. Something went wrong.")
    print("The error is: " + err)
else:
    print("No error detected.")
```

**Want to learn more?**
1. [Starting here] You can also see a brief, interactive tutorial resources at [this link](https://www.w3schools.com/python/python_try_except.asp).
2. [More detailed guide breaking down Exception errors versus syntax errors](https://realpython.com/python-exceptions/)
3. There are many types of Errors that can be handled. You should write your `except` clause to handle each one specifically. Read [this tutorial](https://www.pythonforbeginners.com/error-handling/python-try-and-except) to learn more.

### Exercises

1. Write a `try-except` block that clearly errors and run it. Handle the error by printing something, rather than crashing your program.
2. Learn how to raise an exception using [this tutorial](https://realpython.com/python-exceptions/) and write a `try-except` block where you manually `raise` an Exception in the `try` block and then handle it without crashing in the `except` block.


## Topic 3: `lambda` and `map` and `filter`

**A new way of defining a function: anonymously.**

So far, you've defined functions in the following manner:

```python
def my_function(x, y):
    return x + y
```

This makes a function named `my_function` that can be executed.

However, there's another way to define the same function without creating a named function:

```python
lambda x, y: x + y
```

The above code creates an **anonymous** `lambda` function that adds two numbers given as input, `x` and `y` together and returns it. I know that there isn't a `return` keyword, but `lambda` functions will still return even if you omit the `return` keyword. 

And by **anonymous** I mean that the function has no name. You can't refer to it.

For example, if you defined `my_function` the standard way, you can use it again and again.

But if you define it using the `lambda` keyword, you can't reference it later. E.g., you can't call the function later on in your code.

So why in the world would you want to use an anonymous function?

**Introducing `map()`**

Well, it's most useful when we use it with another built-in Python function called `map()`.

Here's how `map()` works:

```python
map(a_function, some_collection_of_objects)
```

In the line of code above, the built-in `map()` function will apply `a_function` to each and every object in `some_collection_of_objects`.

For example:

```python
def square(x):
    return x * x
    
numbers = [1, 2, 3, 4, 5]

squared = map(square, numbers)

for elem in squared:
    print(elem)
    
# The above prints 1, 4, 9, 16, 25    
```

The above code can be re-written with a `lambda` function in the following way:

```python
numbers = [1, 2, 3, 4, 5]

squared = map(lambda x: x*x, numbers)
```

By using a `lambda` function inside of a `map()`, we save a little bit of code.

You can put some pretty complex stuff inside a `lambda` function. E.g.,

```python
lambda x: x[0] + 2 if x[0] > 100 else x[0] - 2
```

**Introducing `filter()`**

Just like `map()`, there's a built-in Python function called `filter()` that can filter out items from a sequence.

Just like `map()` it works by:

```python
filter(a_function, a_sequence)
```

It will apply `a_function` to `a_sequence` and only keep the ones where `a_function` returned `True`.

For example:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = filter(lambda x: x % 2 != 0, numbers)
```

By combining `map()`, `filter()` and `lambda` functions together you can write some very complex algorithms using very few lines of code.

**Learning more**

1. [Check out this resource with sample code](https://www.python-course.eu/python3_lambda.php)
2. [Shorter tutorial on `map()`, `lambda`, `filter()`, and `reduce()`](https://www.bogotobogo.com/python/python_fncs_map_filter_reduce.php)

### Exercises

Imagine you are programming some software that handles registration of classes at Nueva. You have the following data:

```python
registration = [
    ['Intro to Fabrication', 25, 17],
    ['Advanced Intro to Intro-ing', 8, 15],
    ['Exploring and Understanding Cryptocurrency', 30, 16],
    ['Intro to Intro-ing', 14, 18],
    ['Intro to Data Analysis', 22, 18],
    ['Intro to Mobile App Design', 28, 18],
    ['Advanced Intro to Advanced Advancing', 12, 15]
]
```

The data is structured in the following way: `[class_name, number_interested, max_student_limit]`

Do the following:

1. Imagine someone asks you: "How many classes are still not at full capacity?" 

Write some code that takes in this data, and using some combination of `map()`, `filter()` and `lambda` functions, keeps only the classes where the `number_interested` is smaller than `max_student_limit`.

2. What if someone asks "How many classes have at least 5 roster spots open still?"

Write some code using `map()`, `filter()` and `lambda` to takes in this data and answers this question.