import requests
import lxml.html
from bs4 import BeautifulSoup

# TODO: Before using this script, I HEAVILY suggest you read the first half of this blog post:
# https://brennan.io/2016/03/02/logging-in-with-requests/

s = requests.Session()
login_url = 'https://nuevaschool.instructure.com/login/canvas'

def get_hidden_inputs(session, url):
    """
    This function opens a url and gets all the hidden components, including
    the CSRF token that we need in order to log in.
    """
    login = session.get(url)
    login_html = lxml.html.fromstring(login.text)
    # The below line of code gets the hidden components that we need in order to log in.
    hidden_inputs = login_html.xpath(r'//form//input[@type="hidden"]')
    # This makes part of the dictionary we need.
    form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}
    return form

form = get_hidden_inputs(s, login_url)

# NOTE: We are adding a few other important keys to our data. We're going to
# send this dictionary to the Canvas website.

username = 'cshan'
# TODO: Replace the below with either your password, or make a .txt file called 'password' and put your password there
password = open('./password.txt').read().strip()

# TODO: If you are logging into a website that is NOT Canvas, look at the 'name' attribute of the <form> or <input> element
# and replace the below key names with the relevant name attribute.
form['pseudonym_session[unique_id]'] = username
form['pseudonym_session[password]'] = password

# The below line of code is sending our data (the dictionary we created, including the hidden components)
# to the Canvas login page.
response = s.post(login_url, data=form)

if response.ok: # Checking if you were able to log in.
    print("Your login was successful.")
    soup = BeautifulSoup(response.text, 'html5lib')
else:
    print("You were unsuccessful in logging in.")
