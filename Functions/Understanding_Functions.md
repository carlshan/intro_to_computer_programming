# Understanding Functions
By Carl Shan of [The Nueva School](www.nuevaschool.org)

```python
def add_five(number):
	result = number + 5
	return result
```
*Above is an example of a function that adds 5 to your input, and then returns the result.*

## Introduction

What the heck are functions?

**Imagine this**: Your best friend loves cakes and they wants you to bake a cake for a friend every single day in the month of May. (Okay, that’s a strange example. But bear with me here!) 

Well, since you’re doing it so often, you should probably store the list of ingredients you need and how to assemble them all together. After all, you don’t want to have to remember the list of ingredients and instructions from scratch each time.

Well, **functions are like recipes for programming**: they contain a list of ingredients and instructions that you can use again and again.

![Spongebob](https://media1.tenor.com/images/cce09cde64470bcb416e74136ae62bd2/tenor.gif?itemid=7934757)

**So let's get to cooking with some functions!**


## Understanding Functions

### General Syntax

In general the syntax of a function looks like this:

```python
def my_function_name(input1, input2, input3):

    # Stuff my function does
    # More stuff my function does
    # ...
    # ...
    return something

```

You invoke the function by typing its name and typing parantheses afterwards. Inside these parantheses you put whatever inputs you want to give the function:

```python
my_function_name(5, 10, 123)
```

In the above line of code, I will invoke the `my_function_name` recipe with the inputs `5`, `10`, and `123`.

In programming, inputs to functions are called **arguments** or **parameters**

Okay, now let's look at a real example.

### Function Example

```python
def add_five(number):
	result = number + 5
	return result
```

Here is an example of a function called `add_five` that adds `5` to your input (which we defined to be the word `number`), stores this result in a variable called `result`, and then returns this variable.

Now let's break it down line by line.

![Break it down](https://media1.tenor.com/images/020a7d8eb40482f3edd3aa4e91510944/tenor.gif?itemid=7475588)

### Breaking it Down
We're going to look at each line of code to understand what it does.

`def add_five(number):`

This line defines a function `add_five` and defines it as taking one input. This input is called `number`.

```python
def add_five(number):
	result = number + 5
```

The next line takes the input, `number` and adds 5 to it. It then stores this sum into a variable called `result`.

```python
def add_five(number):
	result = number + 5
	return result
```

The final line returns the variable `result`. When a function returns it value, that means it produces this value as it’s output. 

**Important note**: All functions must return a value! If you forgot to type `return result` in the above function, using the `add_five` function would add 5 to a number, but it wouldn’t produce any result.

It’d be kinda like creating a recipe, but forgetting the last line of your recipe which tells you to take your cake out from the oven after it’s done! Even if you did all the other steps right, you won’t have a cake at the end. 
 
Instead you'll have this:
![Burnt Cake](https://undermangoes.files.wordpress.com/2012/04/img_1468.jpg)

If you forget to `return` a value from a function, the function returns the value `None` by default.

`None` is a built-in Python object that represents the concept of nothing.


### "Calling" your function
When programmers use a function, we say that they are `calling` the function. You can think of it as invoking the function.

Here's how you `call` a function:

`function_name(input1, input2)`

Simply put, you type the function name and put inputs or ingredients in between the parantheses.

For example:

`total = add_five(100)`

The above lines of code runs the `add_five` function with the input `100`, and then stores the output of the function into a variable called `total`.

Congratulations! We’ve just created and used our first function!

Here is a more complex function that performs more operations. What do you think it does?

```python
def what_does_this_do(a, b, c, d):
	if a > b:
		return c + d
	else:
		return (a * b * c) / (d + 2)
```
