# Lists
By Carl Shan, Computer Science teacher at [The Nueva School](www.nuevaschool.org).


## What are lists?
Lists are a type of programming object that hold data. They may be called `arrays` in other programming languages.

Here is an example of a list that we store in a variable called `x`. It contains five different numbers:

```python
x = [5, 10, 8, 12, -5]
```

## Why would we use a `list`?

Why would we use a list? Well since they hold data, it may be very useful to know how to use them.

Here are a few examples of using lists:

### Choosing between different options.
*Example: We'd like to choose randomly between some different colors that we like, so we use a list to hold all of the color options we've chosen.*

```python
import random
import turtle
# here are some colors I want to randomly choose between
colors = ['blue', 'pink', 'purple', 'green', 'red']
random_color = random.choice(colors)
turtle.color(random_color)
```
 
### Running the same code on multiple items
We can create a list of turtle objects and have each turtle in the list move.

```python
import turtle
turtles = [] # creating an empty list that will hold all the turtles

for index in range(500):
	turtles.append(turtle.Turtle())
	angle = 13
	for each_turtle in turtles:
    	each_turtle.right(angle)
    	each_turtle.forward(index)
    	angle += 5
 
```
 
 
### Remembering information as it happens
Maybe we have a command line Python program and we want to remember each thing the user has typed so far, so we can show them the history.

```python
things_said = [] # creating an empty list

keep_going = 'yes'
while keep_going in ['yes', 'Yes', 'YES', 'y', 'Y', 'yeah', 'sure', 'ok']:
	new_thing = raw_input('What do you want to say?\n')
	things_said.append(new_thing)

	print 'So far you have told me:'
	for thing in things_said:
    		print thing

	keep_going = raw_input('Do you want to keep going?\n')
```

Notice that we also used a list to hold all of the possible yes answers.

### Storing large amounts of information

Say you were making a social media app, and you needed to keep track of each users' friends. You might save the name of all the friends in a list.
 
```python
my_friends = ['Jamie', 'Tai', 'Annabelle', 'Lee', 'Jo']
```
 
## Using and manipulating lists
I’m going to create a variable called my_list and set it equal to a list with three items in it.

```python
my_list = ["pizza", "sushi", "sandwich"]
```

0. Getting the length of a list

Use the built-in Python function `len()` to get the length of a list:

```python
len(my_list) # prints 3 since there are 3 items.
```

1. Creating an empty list
To create an empty list in Python, you can just set the variable to empty square brackets

```python
empty_list = []
```

2. Getting elements within a list
To get one item out of a list use the name of the list followed by square brackets with the number inside. 

> This number is called the **index**. 

The first item in the list has the index value of 0.

```python
my_list = ["pizza", "sushi", "sandwich"]
my_list[0] # this gets "pizza"
my_list[1] # this gets "sushi"

# You can also use variables as indices.
number = 2
my_list[number] # this gets "sandwich"
my_list[number - 2] # this gets "pizza"

# You can also use negative numbers to wrap around and get the last element
my_list[-1] # this gets the last element, "sandwich"
my_list[-2] # this gets the second to last element
```

3. Adding things to a list by using `append`
To add an element to the end of a list in Python, use the ‘append’ method.

```python
my_list.append("burger")

#Now the list would be:
["pizza", "sushi", "sandwich", "burger"] 
```

4. Looping over the elements stored inside a list
If I wanted to loop over elements of the list, I can do so easily in a for-loop.

```python
my_list = ["pizza", "sushi", "sandwich", "burger"] 
for food_item in my_list:
	if food_item == "pizza":
		print("One of the foods Carl loves is pizza!")
```

In this for-loop, the variable `food_item` gets created. It gets assigned to each element of the list. 

You can think of the above loop as doing something like the following:

```python
my_list = ["pizza", "sushi", "sandwich", "burger"] 
food_item = my_list[0]
# Do everything in the loop

food_item = my_list[1]
# Do everything in the loop

food_item = my_list[2]
# Do everything in the loop

food_item = my_list[3]
# Do everything in the loop

# for-loop stops since there are no more items in my_list
```

5. Checking if something is in a list
You can also check to see if an element is inside of a list by using the `in` keyword.

```python
a_list = [5, 2, 'hello', 'umbrella', 6]

if 'umbrella' in a_list:
    print("Found the item!")
    
```
The above code, when run, will print `"Found the item"`.

### Learning More About Lists
Use some of these resources to learn more about lists:

0. [Khan Academy](https://www.khanacademy.org/computer-programming/var-array-0-1-2-3-4/957074792)
1. [Google's Tutorial](https://developers.google.com/edu/python/lists)