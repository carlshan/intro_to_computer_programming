# Conditionals
By Carl Shan of [The Nueva School](www.nuevaschool.org)
  
## What are conditionals?
Take a look at this example below.

```python
password = 'despacito'

if password == 'despacito':
    print("Welcome, Luis Fonsi")
else:
    print("You're not Luis Fonsi!")

```

Conditionals are a way for us to check whether certain conditions are `True` or `False`.

## How do they work?

In general, the structure of a conditional works like the following:

```python
if <some condition here>:
    <code that only runs if the condition is True>
else:
    <will run if condition is False>

``` 

Conditions look like the following:

```python
variable == value
```

Note that there are TWO `=` symbols in a conditional.

In Python putting two equal signs like `==` will check for a condition whereas putting a single `=` symbol usually means you're making a variable.

### Another idea: `elif`

Besides the `if` and `else` clauses, you can also have an `else if` clause. In Python it's abbreviated as `elif`.

For example:

```python
name = 'Carl'

if name == 'Carl':
    print("Welcome Carl!")
elif name == 'Beyonce':
    print("Woah! Welcome Beyonce!")
else:
    print("Well, you're neither Carl nor Beyonce.")
```

### Multiple Conditions

What if you want to check for the presence of multiple conditions? 

#### Using the `and` and `or` operator

##### `and`
You can use `and` to join conditions. In this case, the both conditions need to be `True` in order for the `if` block to execute.

```python
username = 'Sam Smith'
password = 'nirvana'

if username == 'Sam Smith' and password == 'nirvana':
    print("Access granted")

```

##### `or`
You can also use the `or` operator to join multiple possible conditions. If you do, then the `if` block will run as long as one of the conditions is `True`.

```python
day = 'Sunday'

if day == 'Sunday' or day == 'Saturday':
    print("It's the weekend!")

```

## What are conditionals, really?

What do you think happens if you ran the following code?

```python
name = 'Carl'

x = name == 'Carl'

```

In the above code we made two variables: `x` and `name`. The value of `x` is set equal to whatever `name == 'Carl'` evaluates to become.

So what is `x` in this situation?

It turns out if you `print()` it, you will get the following:

```python
print(x)

# The above will print 'True'
```

Huh? What's this `True` thing? Is it a word? 

No.

It turns out that Python reserves two values called `True` and `False` that are special values.

They are called Boolean values because they represent the [truth values](https://en.wikipedia.org/wiki/Truth_value), and are named after mathematician and logicial [George Boole](https://en.wikipedia.org/wiki/George_Boole). 

All typical conditions you'll encounter (e.g., things that look like `x == 'something'`) eventually evaluate to become either `True` or `False`. 


