# Intro to Classes

By Carl Shan

## Introduction

What are `classes`?

Now when I say `classes` I don't mean "school classes" as in "Math 1" or "Physics".

I mean `classes` in the programming world.

Well, they look like the below:

```python
class Monster(object):

    def __init__(self, size, name):
        self.size = size
        self.name = name
    
    def speak(self):
        intro = "My name is " + self.name
        return intro
```

Okay. What the heck is going on here?


## What are `classes` and what are they good for?

`classes` are a way of defining some sort of `object` that has certain properties, attributes and can perform certain functions.

**Okay Carl, what do you mean by "defining some sort of `object`"? What's an `object`?**

*Anything* you can come up with can be an `object`. 

**Wait, what?**

That's right. *Anything.* We use `classes` to create representations of other things (e.g., to represent cars, people, monsters in a game, countries).

**Uhhhh ... Okay, I guess that makes sense? ... kinda?**

Alright, I know that's very vague. Here's what I mean by that. 

`classes` allow you to create a _*blueprint for an `object`, and define what sort of attributes and behavior this `object` should have.*_

**Dope. Now gimme an example.**

Coming right up.

## Using `classes` to create a card game

I'm going to give an example of using `classes` by showing how you can write a brief card game using `classes`.

We're going to program a simple card game, but to do that we need some way of representing poker cards in Python.

In your programming journey thus far, you've used things like `lists`, `dictionaries`, `int`s, `str`s and other *data structures.*

`classes` allow us to define *our own data structures and objects*

**Whaddya mean?**

In Python, there's no such thing as a `poker_card` `object` or function. You can't type `poker_card()` in Python and expect it to work.

But by uses `classes`, we'll make our own representation of a poker card. 

**Do this: make a file called `cards.py` and copy the following code inside:**

```python
class Card(object):

    pass

```

There. 

We just defined a `class` called `Card` and it is going to be of type `object`.

This is the general syntax for making a class:


```python
class SOME_CLASS_NAME_HERE(object):

    ### other code here ###

```

Now we're going to do something tricky.

## Part 1: Giving `attributes` to `classes` by using the `__init__()` function

Our `class` `Card` is going to represent a poker card.

![Ace of Spades](http://1.bp.blogspot.com/_JamXY96v8tY/S8hwP4JXp9I/AAAAAAAAAAU/imAocs2Sju8/s1600/ace_spades.jpg)

*Above: Ace of Spades*

Well, what sort of attributes do poker cards have?

They have one of four `suits` (e.g., `['Heart', 'Spade', 'Diamond', 'Club']`) and a `rank` (e.g., `['Ace', 'Two', 'Three' ... 'King']`).

So we want to allow our `Card` class to have these two attributes. Here's how we're going to do so:

**Add the code below.**

```python
class Card(object):

    def __init__(self, s, r):
        self.suit = s
        self.rank = r
```

This code will allow us to create members of the `Card` class that have certain `ranks` and `suits`.

Now if you'll just try and --

**Woah, woah woah Carl! Slow down. How does this code do that?**

Okay fine. Let's break it down line by line.


```
def __init__(self, s, r):
```

This makes a function called `__init__` that takes 3 arguments: some things called `self`, `s` and `r`. The variables `s` and `r` represent a `suit` and `rank` respectively.

These three arguments will be used to `initialize` or `create` our `Card`s.

**What's this `self` variable? What the heck is that?**

Be patient with me. I'm not going to explain that now but I will in a few sections. For now, just assume that it's something we need in order to make our `class` work properly.

I'll explain how in a little bit.

Now, to continue where I lef--

**WAIT! I'm not done Carl ... Why are there two underscores `_` before and after the function name? I've never seen that before.**

Fair question.

Something to just remember about defining `classes` in Python: you need to create a special function called `__init__` spelled *EXACTLY* like that.

**Okay. But what is this `__init__()` function? What makes it so special.**

This function `initializes` objects of our `class`. That's why it's called the `__init__()` function.

By `initialize` I mean *to create* an *instance* of our `Card` class.

By using this function later, we will be able to 

**Hold up. What are you talking about?**

Think about `classes` like this: they are a blueprint for objects we are later going to build.

In the blueprint we get to specify exactly what attributes our objects need to have.

The `__init__()` function is special because it's the function that does the actual `construction` of these objects. It `constructs` or `initializes` actual things built with this blueprint.

In programming lingo, we say that we *initialize an instance of the `Card` class.*

**Derp. What? I'm not following. What do you mean by "initialize an `instance` of a `class`"?**

Later on you will see code that looks kinda like this:

```python
a_card = Card(s='Spades', r='Ace')
```

That code above `initializes` an `instance` of the `Card` class that has a `rank` of `"Ace"` and a `suit` of `"Spades"`. 

We then assign this instance to a variable called `a_card`.

When we do this, we are actually implicitly calling the `__init__()` function to construct this instance. 

Don't worry if you're still confused! `classes` are a hard computer science topic to understand! It's okay if you don't get it the first time around. Most people don't.

I definitely didn't.

By working through this tutorial and the below exercises, you will come back to these ideas again and again and hammer in these bolts of knowledge so that you build a sturdy foundation on which you will be able to create a tower of insight and learning.

**Dang Carl, you're really taking this building metaphor kinda far.**

Yeah, well, whaddya gonna do? Sue me? (Please don't.)

**Okay okay. Alright. What was the point of all this again?**

Okay, to bring this back to the original point, I want to explain just this line:

```
def __init__(self, s, r):
```

This creates an important function that all classes need to have called the `__init__()` function (also known as the `constructor`) that takes three inputs, and we will use this function when initialize an instance of the `Card` class.

**What about the next few lines of code?**

```python
def __init__(self, s, r):
    self.suit = s
    self.rank = r
```

What does the lines `self.suit = s` and `self.rank = r` mean?

Basically, they allow us to create the attributes `.suit` and `.rank` on a `Card` instance, and assign the values of `s` and `r` to them respectively.

Going back to this line of code:

```python
a_card = Card(s='Spades', r='Ace')
```

It essentially is doing the following:

```python
a_card = __init__(s='Spades', r='Ace')
```

Now if we try the following, we can access the `.suit` and `.rank` attributes and get the following results:

```python
print(a_card.suit)
# prints 'Spades'

print(a_card.rank)
# prints 'Ace'
```
**Carl. I'm gonna be honest with you. I still don't understand everything. And thid was a lot of content. Couldn't you, like, gimme a  a summary or something?**

*Sigh.* Alright your Majesty. One summary coming up.

## Summary of Part 1

1. In Python, you create classes with `class SOME_NAME_HERE(object):` followed by code.
2. There's a special function that you need to define called `__init__` that is the `constructor` and is invoked every time someone creates an *instance* of a `class`.
3. You add attributes to members of a class by using `self.something` in the `__init__()` constructor. E.g., `self.suit = s`.
4. You create an instance of the `class` by typing the name of the `class` followed by the required arguments that the constructor needs (e.g., `a_card = Card(s='Spades', rank='Ace')`).


## Practice Exercise for Part 1

To make sure you've actually learned and understood Part 1, try the following exercise:

Create a `class` called `Pet` that has the following attributes:

* `.name` attribute (e.g., `'Fido'`, `'Furball'`)
* `.size` attribute (e.g., `'large'`, `'medium'` or `'small'`)
* `.favorite_food` attribute (e.g., `'bones'`, `'my homework'`)

Then create an instance of this `Pet` class, and give this instance a `.name`, a `.size` and a `.favorite_food`.

Call me over when you're done so that I can check to make sure you're on track.


## Part 2: `methods` and behaviors of `classes`.

In this section, we will learn how to define behaviors that members of the `class` can take.

Right now, your code should look something like:

```python
class Card(object):

    def __init__(self, s, r):
        self.suit = s
        self.rank = r
        
a_card = Card(s='Spades', r='Ace')
```
We want to define other functions on our `Card` class, not just the `__init__()` constructor.

Whenever we make a function inside of a class, it has a special name. We call taht function a `method`. 

We're going to define a `method` called `get_value()` that will print a helpful description of the card.

Add this function into the `Card` class:

```python
class Card(object):
    
    # the __init__ code here
    
    def get_value(self):
        card_value = self.rank + " of " + self.suit
        return card_value
```

Now we can use this `get_value()` method (remember, functions defined inside of classes are called *methods*, not simply functions):

```python
a_card = Card(s='Spades', r='Ace')

print(a_card.get_value())
# prints "Ace of Spades"
```

**Wait Carl. How did this `get_value()` method work?**

Now I am going to explain this `self` variable and use it to show how everything links together.

The `self` variable is a built-in variable in Python `classes` and it allows you to refer to an `instance` of the class.

So to explain when you type:

```python
def get_value(self):
    card_value = self.rank + " of " self.suit
    return card_value
```

When you type `self.rank` and `self.suit`, those two variables basically mean *"get the attributes .rank and .suit of the instance that the `get_value()` method is being invoked with"*.

**Wait. Huh?**

Here. Try this:

```python
card1 = Card(s='Clubs', rank='Two')
card2 = Card(s='Spades', rank='Three')

print(card1.get_value())

print(card2.get_value())
```

Wait. How come they printed different things?

Even though both of them are using the same `.get_value()` method, different things got printed because `self.rank` and `self.suit` is different for the two cards. And `.get_value()` will use the corresponding `self.rank` and `self.suit` for each of the cards.

**So what does this mean about the `self` variable?**

The `self` variable is basically a way for Python classes to refer to specific instances. It allows you to refer to the attributes of the specific instance.

**Okay ... **

Here's the thing to remember.

If your method needs to use the `self` parameter, you *need* to make sure that's the first argument that the method takes.

For example, take a look at the `get_value()` method again:

```python
def get_value(self):
    # code here
```

Since I knew that this function was going to print the value of the card, it needed to use the `self` variable to get the specific `self.rank` and `self.suit`. So this `get_value()` function needed to take the `self` parameter as input.

**Another summary please!**

## Summary of Part 2

* Classes don't just have attributes. They can have functions that we can methods.
* Methods are defined just like regular functions (e.g., `def some_function()`)
* Methods can access the `self` variable to get the specific value for different instances.
* If you are writing a method that needs to access specific attributes of different instances, make sure to take the `self` argument as input and use it in the function (e.g., the `get_value()` method above).

## Practice Exercise for Part 2

Define a class called `Deck`. It should have the following:

1. An attribute called `.cards` which is a list that contains all 52 possible poker cards (e.g., `Ace of Spades` and `Jack of Hearts`) 
    * **HINT:** Use a few for-loops to generate all these cards. Don't type them all out by hand.
2. A method called `draw_card()` that returns the last item in `self.cards`.
3. A method called `add_card()` that appends a card to `self.cards`.
4. A method called `shuffle` that randomly shuffles `self.cards`
    * **HINT:** Take a look at the `random` module in Python and see how it can help you randomly change the order of items in a list.

Make sure to raise your hand and ask questions when you need to! These are not always easy.

## Assignment Exercises

### Standard

Just complete and turn in the exercises for `Part 1` and `Part 2`. 

### Intermediate

Finish the exercises in `Part 1` and `Part 2`

Then, using the `Card` and `Deck` class, create a simulation of the game `Blackjack` (AKA 21). If you are unfamiliar with this game, you can watch this [5 minute video explaining the game](https://www.youtube.com/watch?v=-9YGKFdP6sY).

Or you can recreate another game. Make sure you let me know what you are thinking before you start, so I can let you know if it may be too ambitious.

### Advanced

Create as close to a simulation of the game of Texas 'Hold Em, or another variant of Poker that you would like.

You don't have to implement any betting in the game.

However I should be able to play a round in your game (e.g., I should be able to draw a hand, and compare my hand to yours. Whichever one is higher "wins" the round.)

To do this you will need to write code that checks for which hand is higher.

You can see a full list of Poker hands from highest to lowest on this [webpage](https://www.pokerstars.com/poker/games/rules/?no_redirect=1).

