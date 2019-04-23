# Recursive Functions Exercises
By Carl Shan

Pick one set of exercises to complete.

## Intermediate

1. Remember the Fibbonaci sequence? Write a recursive function called `fib` that takes as input a number `n` and generates the `nth` Fibbonaci number.

The Fibonacci sequence starts with: `1, 1, 2, 3, 5, 8 ...`

Example:

```python
fib(5)
# should print 5

fib(7)
# should print 13

fib(25)
# should print 75025
```

2. Make a recursive function called `countdown` that takes a number `n` as input and prints `n`, `n-1` ... until it reaches `0`.

Example:

```python
countdown(5)
# the above should print
# 5
# 4
# 3
# 2
# 1
```

3. Make a recursive function called `recursive_sum` that takes a list `l` as input and computes the sum of the list in a recursive manner.

Example:

```Python
recursive_sum([1, 2, 5, 9])
# should return 17
```


## Advanced


1. Write a function called `recursive_max` that takes a list of integers as input, and recursively finds the max of that list.

Example:

```python
# List with even size
A = [7, 1, 9, 0, 8, 2, 5, 3, 4, 6]
# List with odd size
B = [7, 1, 9, 0, 8, 2, 5, 3, 4, 6, 10]
# List wih only 2 elements
C = [4, 6]
# List with only 1 element
D = [7]
# Empty list
E = []
 
# Call the function
print "Max of A = {}".format(recursive_max(A))
print "Max of B = {}".format(recursive_max(B))
print "Max of C = {}".format(recursive_max(C))
print "Max of D = {}".format(recursive_max(D))
print "Max of E = {}".format(recursive_max(E))


# The above prints:
# Max of A = 9
# Max of B = 10
# Max of C = 6
# Max of D = 7
# Max of E = None

```


2. Write a recursive function called `reverse_list` that takes a list of elements and reverses them.

Example:

```python
A = [1, 2, 3, 4, 5]
B = ["Hello", "There", "!"]
C = [1]
D = []

print(reverse_list(A))
# prints [5, 4, 3, 2, 1]
print(reverse_list(B))
# prints ["!", "There", "Hello"]
print(reverse_list(C))
# prints [1]
print(reverse_list(D))
# prints []
```

3. Define a recursive function called `flatten` that takes in a list, flattens the list and returns the flattened version as a new list.

>**NOTE**: To flatten a list means to take a list of lists (of lists, of lists ...) and put them all in one list.

Example:

```python
c = [1, 2, 3, [4, 5, 6]]

print(c)
# prints 

print(len(c)) 
# prints 4, but we know that the 4th element is itself another list

flatten(c)
# returns [1, 2, 3, 4, 5, 6]


k = [1, 2, [3, 4, [5, 6, [7]]]]
flatten(k)
# returns [1, 2, 3, 4, 5, 6, 7]

```


