# Introduction to Dictionaries
By Carl Shan, Computer Science teacher at [the Nueva School](www.nuevaschool.org).

## What are dictionaries?
A dictionary is a type of programming element that allows you to associate bits of data with other bits of data. 

In programming lingo, this can be described as "associating keys with values."

Woah. What?

Well, remember when we were working with lists? 

([If you don’t you can refresh your memory by clicking here.](https://github.com/carlshan/intro_to_computer_programming/blob/master/Lists/Lists_Tutorial.md))

Well you can think of lists like a big box of stuff. It just holds a lot of data.

See the box below. It holds ... a surprise.

![Box of Stuff](https://media1.tenor.com/images/bb3e64ee16c825ac127bd4b573d024d1/tenor.gif?itemid=8451858)

Okay, so that's what lists are. They are boxes of data.

Dictionaries are like boxes that hold stuff but with a twist ... they allow you to label the data!

![Labeled data](https://www.vistaprint.com/sf/_langid-1/_hc-00003a5c/_/vp/images/b13/category-pages/labels-stickers/product-tiles/product-labels-001.jpg)

Look at this. Now these products are labeled!

### More technical description
Dictionaries are objects that store pairs of values. 

These pairs are called `'key-value'` pairs.

You will use dictionaries to hold information if you want the information to be associated with some other piece of information.

For example, you may use a dictionary to hold information about a person's username and their password.

In that case, the username is the `key` and the password is the `value`. Together, the username and password forms a `'key-value'` pair.

Now let's learn about how to use a dictionary.

## Syntax
### Creating an empty dictionary
I'm going to create an empty dictionary. I'll assign it to a variable called `bank`.

```python
bank = dict()
```

Alternatively, I can also create an empty dictionary by:

```python
bank = {}
```

Both will do the same thing.

This dictionary will hold pairs of information, associating a `key` with a `value`.

### Adding to a dictionary: Creating an in the bank

So far our bank is empty. It has no account holders. Let's say I want to sign up to for an account at this bank.

To add a `key-value` to a dictionary, you need a `key` and a `value`.

I will tell Python that I want it to create a `key` called `'Carl'` and give this `key` a value of `100000`. 

```python
bank['Carl'] = 100000
```

In my example above, my `key` is `'Carl'` and the value associated with that `key` is `100000`.

I'm a wealthy man!

### Increasing my balance: Changing the value associated with a key

This is how you change the amount of money I have

```python
bank = dict()
bank['Carl'] = 0 # I'm very poor!
bank['Carl'] = bank['Carl'] + 1000
```

### Modifying all accounts: Looping over a dictionary

Remember that you can make a list and write a for-loop to access every element of the list?

If you don't, refresh your memory with the example below:

```python
myList = [1, 'hello', 99, 'apple']

for element in myList:
    print(element)
```

This program will print each element in the variable `myList` one-by-one. You can learn more by visiting [the lists tutorial here](https://github.com/carlshan/intro_to_computer_programming/blob/master/Lists/Lists_Tutorial.md).

It turns out that you can do something similar with dictionaries ... except there's a catch.

When you write a for-loop over a dictionary, you're looping through all of the KEYS.

For example, what do you think the below will result in?

```python
bank = dict()
bank['Carl'] = 1000
bank['Abigail'] = 2000

for key in bank: 
  print key
```

The for-loop will print `'Carl'` then `'Abigail'`.

So keep that in mind.

A for-loop will access the **keys** of the dictionary. **NOT** the values.

### Removing data from a dictionary

Finally here's how you delete a key from the dictionary

```python
bank = dict()
bank['Delete Me!'] = None

del bank['Delete Me!']
```

The `del` keyword allows you to remove a key-value pair from a dictionary.

## Additional Resources
To learn more about dictionaries, you can use the tutorials below:

1. Beginner - [LearnPython.org](https://www.learnpython.org/en/Dictionaries)
2. Beginner/Intermediate - [Python-Course.eu](https://www.python-course.eu/dictionaries.php)

