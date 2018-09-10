# Loops
By Carl Shan of [The Nueva School](www.nuevaschool.org)

## What are loops?

In programming, we use loops to repeat blocks of code.

![Loop](https://cdn3.iconfinder.com/data/icons/transfers/100/239329-loop_repeat_refresh-512.png)

There are two types of loops in Python you'll frequently see:

#### The `while` loop

This loop executes as long as some condition is true.

```python
x = 1

while x < 10:
    print('How many times does this get printed?')
    x = x + 1
```

In the above example, the instructions inside of the loop will be executed as long as the condition `x < 10` remains true.

**Question**: How many times does the above get printed? Are you sure? 

#### The `for` loop

A `for` loop is traditionally used to run a block of code a set number of times, rather than until a condition is done.

```python
for x in range(0, 5):
    print('How many times does this get printed?')

```
