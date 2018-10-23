# Introduction to APIs

By Carl Shan of [The Nueva School](www.nuevaschool.org)

In this tutorial you will learn what an API is, and also how to write programs that use the Canvas and Twilio API to send text messages to yourself when you have an assignment due.

# What are `API`s anyways?
API stands for "Application Programming Interface". 

"Uhhh ... that's not very helpfull. What does that mean?"

It sounds complicated, right? Well lemme break it down for you.

Basically, an API is a set of rules that some software has about how other software can talk to it.

It's basically an "Instruction Manual" for some software, website or app.

For example, below is a set of instructions for parents.

**Example: The "Parenting" API**

![Parenting Manual](https://github.com/carlshan/intro_to_computer_programming/blob/master/Images/clever_api.png?raw=true)

Like the examples above, many pieces of software also have examples of "Good" and correct ways of using that software.

Most large software companies have an API that is specific to their product. 

My first job out of college was working for an education startup called [Clever](https://clever.com/) that built and sold an API for school districts (so that other education software companies could integrate with schools all over the country).

Here's a picture of Clever's website where they describe a part of their API:

![Clever API]()

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

FIrst, you're going to have to `pip install --user twilio` in Terminal.

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
* Next, you will need the `canvasapi` Python library. Go into Terminal and `pip install --user canvasapi`.
* Next, you will need to set up the following code:

```python
from canvasapi import Canvas

API_URL = "https://nuevaschool.instructure.com/"
API_KEY = "YOUR API KEY HERE"

canvas = Canvas(API_URL, API_KEY)
```

Great, now you will need to figure out how to combine the two together.

Here's what you have to do:

# Exercises: 

1. Write some code that gets all of the assignments from a particular class.

**HINT:** To do this you will need to learn how to use the `canvasapi` Python library that you installed. Specifically, you will need to use this link: [`canvasapi` documentation](https://canvasapi.readthedocs.io/en/latest/)

2. Write code that finds the due date of each assignment. 

**HINT:** Check to see if there's a function that's in the `canvasapi` library that helps you with this.

3. Write a program that texts you a few days ahead of time of an assignment being due using what you learned from above.

**HINT:** You will need to learn about how to use the `datetime` module that's built into Python. (See here for a [starter tutorial](https://www.w3schools.com/python/python_datetime.asp), though you will probably need more than just this). 

4. If you were able to complete steps 1-3, build some programs that can actually help you get work done. For example, maybe you could build something that texts you your schedule every day? Since many students rely on their Google Calendar, which has its own API in addition to a Python library. You can see how you can get started here: [Google Calendar API & Python Support](https://developers.google.com/calendar/quickstart/python).



