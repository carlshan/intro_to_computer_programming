# Introduction to APIs

By Carl Shan of [The Nueva School](www.nuevaschool.org)

In this tutorial you will learn what an API is, and also how to write programs that use the Canvas and Twilio API to send text messages to yourself when you have an assignment due.

# First, install Python 3
We're going to use Python3 instead of Python2 for this tutorial.

That's because one of the Python libraries we're using requires Python3. 

Visit www.python.org and download Python version 3.7 to your computer and run the installer.

As a result of this, you'll have to use `pip3` instead of `pip` to install packages.

You can also run python scripts with Python3 by typing `python3 some_file.py` in Terminal instead of `python some_file.py`.

You should now also upgrade `pip` to the latest version as well:

`
pip3 install --upgrade pip
`


# What are `API`s anyways?
API stands for "Application Programming Interface". 

"Uhhh ... that's not very helpfull. What does that mean?"

It sounds complicated, right? Well lemme break it down for you.

Basically, an API is a set of rules that some software has about how other software can talk to it.

It's basically an "Instruction Manual" for some software, website or app.

For example, below is a set of instructions for parents.

**Example: The "Parenting" API**

![Parenting Manual](http://cdn.emgn.com/wp-content/uploads/2014/02/Funniest-Parenting-Instructions-Feature.jpg)

Like the examples above, many pieces of software also have examples of "Good" and correct ways of using that software.

Most large software companies have an API that is specific to their product. 

My first job out of college was working for an education startup called [Clever](https://clever.com/) that built and sold an API for school districts (so that other education software companies could integrate with schools all over the country).

Here's a picture of Clever's website where they describe a part of their API:

![Clever API](https://github.com/carlshan/intro_to_computer_programming/blob/master/Images/clever_api.png?raw=true)

If you want to browse more, you can check out [Clever's API here](https://dev.clever.com/reference).

## Wait, do I already use `API`s in my life?

"Well, that's interesting Carl. What's an example of an API in my life?"

**Spam Calls**: You know how you sometimes get spam text messages or phone calls?

Someone wrote a program that uses some texting or phone call API to robo-spam people.

**Phone Notifications**: You know when you get a notification from Snapchat or Instagram? That's Snapchat coordinating with your smartphone's API to send you a message.

**Your `pyautogui` program**: Oh wait, you know how you've been using `pyautogui`? 

Turns out, `pyautogui` controls your laptop by using your computer's API for controlling your mouse, keyboard etc.

Cool.

So you have maybe a better idea of APIs.

Now let's learn how to use some APIs to do something nifty.

## What you will learn how to do

By the end of this tutorial, you will know how to write a program that sends text messages to yourself 2 days before an assignment is due on Canvas.

![Finished Product](https://github.com/carlshan/intro_to_computer_programming/blob/master/Images/api_example.png?raw=true)


# Things you will learn:

1. **Twilio's API**: How to write Python code that uses an API made by a company called Twilio to send text messages.
2. **Canvas API**: How to use the Canvas API to get the assignments for your class.
3. **Using them together**: How to use them both to text you reminders about when assignments are due.


## Step 1: Sign Up For Twilio

"Uh Carl, what's Twilio? I've never heard of it before Is it sketch?"

Twilio is publicly traded tech company that builds APIs for text messaging, voice calls and more.

So no. It's not sketch.

In fact, it's the opposite. 

As I've heard some of my students say, "it's *lit*."

Okay. Here's what you're going to do:

1. First sign up for a Twilio account [here](https://www.twilio.com/try-twilio)
2. Next, enter your phone number that you want to receive text messages (leave the box below unchecked if you don't want to get spam)
3. Verify your phone number by entering the code that Twilio texts you.
4. After this, you should be logged in.
5. Now go to Twilio's Console by clicking "Console" in the top right corner.
6. Copy your Account SID and Auth Token to a separate document. We'll be using this soon.
7. Click on "Phone Numbers" on the left-hand panel and then click on "Manage Numbers"
    * Click on "Get Started"
    * Click on "Get your first Twilio phone number"
    * Now Twilio will find you a free phone number.
    * Click on "Choose this number" afterwards
    * Great! You now have a Twilio phone number that can text you messages!
    * Click on "Manage Numbers" again. You should see the phone number listed.
    * Copy this phone number into a separate document. We'll use this soon too.

Now we're going to take all this

## Step 2: Make a Python program

We're going to combine all this together to write a short Python program that texts you a message from your Twilio number.

**Installing the `twilio` library:** 

FIrst, you're going to have to `pip3 install --user twilio` in Terminal.

Make sure you do that.

**Make a Python file**

Name the file `text_message.py`. Copy in the following code:

```python
from twilio.rest import Client

# Copy your account Sid and Auth Token from twilio.com/console
account_sid = 'YOUR ACCOUNT SIDE HERE'
auth_token = 'YOUR TOKEN HERE'
client = Client(account_sid, auth_token)
```

**Replace the `account_sid` and `auth_token` variables with your values**

Remember when you went into the `Twilio Console` and found your Account SID and Auth Token?

If not, go to [Twilio's Console](https://www.twilio.com/console/) and find them.

Now copy the relevant values into the code to replace the variables.

For example, your code might look like:

```python
account_sid = 'AC5abcedfasfsaljfksdajlkfsdj'
auth_token = '0c9f3ngiasdjfaldfadslfdsdfsasdf5'

```

The SID and Auth Token are basically the equivalent of your *username* and *password* when using Twilio's API.

In fact, most APIs will require you to sign up and get an SID or Auth Token. 

**"Logging in" with our credentials**

Now we can "log in to the API" with these credentials.

Here's how you log in. Add the line of code below into your program:

```python
client = Client(account_sid, auth_token)
```

If you get an error that `Client` is not defined, you probably forgot to include the following line of code at the top of your program:

```
from twilio.rest import Client
```

**Actually texting someone**

We're going to text yourself a message from your Twilio phone number now.

Add the code to bottom of your program.

```python
text = "You are awesome."
twilio_num = "YOUR TWILIO PHONE NUMBER HERE" # e.g., '+16696002352'
my_phone = "YOUR ACUTAL PHONE NUMBER HERE" # e.g., '+14081234567'

message = client.messages.create(body=text, from_=twilio_num, to=my_phone)
```

This will use the Twilio API to send a message from one number to another.

Now run this program!

You should receive a text message within a few seconds.

Congrats, you just used the Twilio API!

## No spamming
Don't write programs that spam people. Full stop.

Fortunately Twilio also has some built-in safe measures against spamming.

Something that's built into Twilio is that you can only send messages from the Twilio phone number, and only to phone numbers that are Verified Caller IDs on the Console. This way you can't spam people but you can use it yourself.

# Step 3: Using Canvas' API

Now that we have successfully used Twilio's API to send a text message, we're going to use the Canvas API to get a list of all of the assignments that are due.

This part of the tutorial will walk you through the intro steps, although you will have to figure out the rest on your own.

* First, you will also need to get a Canvas API key (this is your API password). Follow the [instructions here to get a key](https://community.canvaslms.com/docs/DOC-10806-4214724194).
* Next, you will need the `canvasapi` Python library. Go into Terminal and `pip3 install --user canvasapi`.
* Next, you will need to set up the following code:

```python
from canvasapi import Canvas

API_URL = "https://nuevaschool.instructure.com/"
API_KEY = "YOUR API KEY HERE"

canvas = Canvas(API_URL, API_KEY)
```

This will create a variable called `canvas` that represents the `Canvas` object that has all of the relevant functions you can use to complete the exercises.

Now you will need to figure out how to combine the Twilio code and the Canvas code together.

Below are exercises that help you figure out how to combine things.

# Exercises: 

Do and turn in exercises 1 - 4.

If you are done, try the Bonus Creative Challenge exercise.


## Exercise 1. Write code that gets a particular class that you're enrolled it.

To do this you will need to learn how to use the `canvasapi` Python library that you installed. Specifically, you will need to use this link: [`canvasapi` examples](https://canvasapi.readthedocs.io/en/latest/examples.html). Scroll around and see if you can find something you'll use.

If you succeed, part of your code should look something like the following:

```python
canvas = Canvas(API_URL, API_KEY)

course = ________________ # figure out what goes here

```


## Exercise 2. After completing exercise 1, write code that prints all the assignments in that class.

You want to figure out how to get a list of all assignments from a particular class.

Maybe there's soemthing that's in the `canvasapi` library that helps you with this?

When you succeed, your code should look something like this:


```python
course = ________________ # figure out what goes here

assignments = course._________________ # figure out what goes here

for assignment in assignments:
    print(assignment)

```

If your code is correct. The above should print something like the below:

```
Complete the intro survey (28547)
Submit your personal website (29266)
Submit an image and a Python file of your complex shape (29554)
Turn in your lists assignment (29667)
Turn in your Functions assignment (30131)
Turn in your Dictionary assignment (30467)
Turn in your midsemester project (30847)
Turn in your API assignment (31586)
```

### Exercise 3: Getting the due dates for each assignment

Now write some code that prints the due dates for each of the assignments.

If correct, your code should look something like:

```python
for assignment in assignments:
    due_date = assignment._______________ # figure out what goes here
    print(due_date)
```

And the above should print something that looks like:

```
2018-09-06T06:00:00Z
2018-09-13T05:00:00Z
2018-09-19T05:00:00Z
2018-09-29T05:00:59Z
2018-10-06T05:00:59Z
2018-10-24T05:00:59Z
2018-11-06T07:59:59Z
```

**HINT:** If only there was a command in Python that would show you all of the attributes and functions you an use on an object ... turns out, there is! It's the `dir()` function. By passing an object as the input to the `dir()` function, it prints out all of the attributes and functions available for you to use.

Print the result of the `dir` function on an `assignment` (e.g., `print(dir(assignment))` after you've made a variable called `assignment` that stores one particular object to see all the available functions that you can use. There is something in here that is probably what you want.

### Exercise 4. Write a program that texts you a few days ahead of time of an assignment being due using what you learned from above.

You will need to use your knowledge of the Twilio library and code to solve this problem.

You will also need to learn about how to use the `datetime` module that's built into Python. (See here for a [starter tutorial](https://www.w3schools.com/python/python_datetime.asp), though you will probably need more than just this). 

If you're successful, your code should look something like the following:

```python
from twilio.rest import Client
from canvasapi import Canvas
import datetime

# ... some code here ... #

due_date = assignment.__________ # figure out what goes there
today = datetime.datetime.now()

days_until_due = (due_date - today).days

if days_until_due == 2:
    # ... use Twilio text yourself which assignment is due and in how many days... #
```


### Creative Challenge: Build something useful for you

If you were able to complete steps 1-3, build some programs that can actually help you get work done. 

For example, maybe you could build something that texts you your schedule every day? 

Since many students rely on their Google Calendar, which has its own API in addition to a Python library. You can see how you can get started here: [Google Calendar API & Python Support](https://developers.google.com/calendar/quickstart/python).


## Common Issues and Bugs

Use this section to debug issues you're getting.

### Issue: When I press `Command` + `I` in Atom to run my code, it says "No module named `canvasapi`" or "No module named `twilio`"

This is happening because the Script addon in Atom is running your program using Python2 instead of Python3. 

You are going to change the script addon to use Python3.

In Atom, click on `Packages` > `Script` > `Configure Script`

And in the `Command` box, type `python3`.

Now press the `Run` button and your script should run with Python3 instead of Python2.

### Issue: No module named `twilio` or No module named `canvasapi`

This likely happened because, after you downloaded Python 3 from [Python.org](www.python.org), you didn't reinstall the `twilio` and `canvasapi` libraries using `pip3`.

**Solution:** 

We need to reinstall the two libraries using `pip3` instead of `pip`. `pip3` is for Python3.

`pip3 install canvasapi`

`pip3 install twilio`

As long as these don't error, you should be able to continue.

### Issue: When using `pip` to install libraries, you get an error like `[Errno 13] Permission denied /Users/cshan/Library/Python/3.7`

This is because the `root` user of your computer owns that folder and is the only user who can modify it, and the user you're logged into (e.g., `cshan` for me) isn't `root` and can't modify this folder.

**Solution:**
We're going to enable your user to modify these files.

In Terminal type:

`sudo chown -R $USER <<COPY YOUR PATH HERE TO THE 3.7 FOLDER>`

Where you replace the `<< ... >>` with the actual path to your Python 3.7 folder.

For example:

`sudo chown -R $USER /Users/<<your Terminal username here>>/Library/Python/3.7`

And replace `<<your Terminal username here>>` with your actual Terminal username. 

(**NOTE:** You can find out your username by typing `echo $USER` in Terminal.)

In the end, the command should look something like like:

`sudo chown -R $USER /Users/cshan/Library/Python/3.7`

Now if this runs correctly you should be able to `pip` install correctly without any issues.

