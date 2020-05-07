# Automating things on your computer with PyAutoGui
By Carl Shan of [the Nueva School](www.nuevaschool.org)

## Intro

This tutorial will teach you how to use the `pyautogui` library to automate things on your computer.

## What is `pyautogui`

`pyautogui` is a Python library (meaning, a bit of code that someone else has written and made available) that implements a number of functions allowing you to automate things on your computer.


## Setup and Installing

To setup `pyautogui` we need to do the following:

Step 1: Installing `pip`

* `pip` is the Python package installation manager. It's like the App Store for Python. It allows us to install Python tools. We need to get and install `pip`.
* In your Terminal, type `sudo easy_install pip`
* Enter your password and press Enter

Step 2: installing `pyautogui`

* Now we're going to use `pip` to install `pyautogui`.
* First, let's setup some things that `pyautogui` needs
    * In Terminal type `pip install --user pyobjc-core`
    * Then type `pip install --user pyobjc`
* In Terminal type `pip install --user pyautogui`


## We now have `pyautogui` installed!

Now, as long as you type `import pyautogui` at the top of any Python file that uses it,  you'll hve access to `pyautogui`'s commands.

So what can it do?

## All of `pyautogui`'s functions

If you want to read about all that `pyautogui` can do, you should look at this website: [Here's the official PyAutoGui website that details all the things that you can do with it.](https://pyautogui.readthedocs.io/en/latest/cheatsheet.html).

Specifically, I encourage you to look at the following tutorials:

0. [Quick reference cheat sheet](https://pyautogui.readthedocs.io/en/latest/cheatsheet.html)
1. [How to control your mouse](https://pyautogui.readthedocs.io/en/latest/mouse.html)
2. [How to control your keyboard](https://pyautogui.readthedocs.io/en/latest/keyboard.html)
3. [Message box functions](https://pyautogui.readthedocs.io/en/latest/msgbox.html)

## 5-min tutorial to `pyautogui`

I've outlined a few example of things you can to do:


### Important Note
**IMPORTANT**: If you ever write a program in `pyautogui` that you need to shut down, move your mouse to the top-left corner of your screen.

That's `pyautogui`'s failsafe. You'll break out of it.

### Clicking your mouse
```python
import pyautogui

# # This will click your mouse
pyautogui.click(button='left', clicks=2, interval=0.25)

## This will click your right mouse twice with a delay of 0.25 seconds between each click
pyautogui.doubleClick(button='right')

```

### Moving your mouse and then clicking


```python
# This will slowly move your mouse to 500, 500 over the course of two seconds
pyautogui.moveTo(x=500, y=500, duration=2)

# Then you can click on something.
pyautogui.click(button='left')
```


### Using Hotkeys

```python
# This will press CMD + C (AKA copy)
pyautogui.hotkey('command', 'a')
pyautogui.hotkey('command', 'c')
```

### Typing something

```python
# Here's how you type something. It'll type the text below with an interval of
# 0.1 seconds between letters.
pyautogui.typewrite("Yeah, I'm awesome.", interval=0.1)
```

### Figuring out where your mouse is

```python
# Here's how you get the width and height of your screen
width, height = pyautogui.size()

# Here's how you get the X and Y value of your mouse
mouse_x, mouse_y = pyautogui.position()
```

In addition if you need to locate the exact coordinates of something on your screen, you can press `Command + Shift + 4` to bring up the screenshot tool. This tool will also have numbers underneath the crosshairs indicating the `x` and `y` coordinates of wherever your mouse is hovering over.


## Additional Resources
If you want to see what else PyAutoGui can do, see the following: 

1. [Here's the official PyAutoGui website that details all the things that you can do with it.](https://pyautogui.readthedocs.io/en/latest/).
2. [*Automate The Boring Stuff* by the author of PyAutoGui](https://automatetheboringstuff.com/chapter18/)
