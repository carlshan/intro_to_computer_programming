# Dictionary Assignments


## Exercises:

### Beginner:
**Exercise 1.** Practice the syntax of dictionaries by:

* Creating an empty dictionary called `'my_information'`
* Add the key `'my_favorite_class'` to the dictionary and have the value be the name of your favorite Nueva class
* Add the key `'my_favorite_color'` to the dictionary and have the value be the name of your favorite color
* Write a for-loop over this dictionary and print out each key and value in the dictionary

### Intermediate:
**Exercise 1.** Create a function called `change_dictionary` that takes a dictionary as input. This function should then add `2` to each value of the dictionary.

EXAMPLE:

```python
my_dict = {'carl': 100, 'justin_bieber': 5}
change_dictionary(my_dict)

print(my_dict)

# The above should print {'carl': 102, 'justin_bieber': 7}
```

**Exercise 2.** Create a function called `count_appearances()` that takes two inputs: a list and a dictionary.  This function should modify the dictionary so that it counts the number of times an element appeared in the list.

EXAMPLE:

```python
def count_appearances(counter, list_to_count):
    # This function should loop over list_to_count and increment the value
    # associated with the key that is being looped over and increment it by one each time
    "***YOUR CODE HERE***"
   

counter = {'carl': 0, 'joe': 1, 'scott': 0, 'cristina': 1}
people = ['carl', 'carl', 'scott', 'cristina']
count_appearances(counter, people)

print(counter)
# If your function works, then the above should print {'carl': 2, 'joe': 1, 'scott': 1, 'cristina': 2}
```

### Advanced:
**Exercise 1.** Write a function called `check_password()` that takes three inputs: a username, a password and a database. This function checks to see if a password corresponds to a username in a database. This database will be represented as a dictionary.

The function should return `False` if the password does not match to the username, and `True` if the password is correct.

EXAMPLE:

```python
# This is a database of my username-password pairs.
my_database = {
            'Carl': 'iamsuperman',
            'Abigail': 'mypasswordisawesome',
            'Scooby': 'ilovechickenpie',
            'Justin Bieber': 'selenagomez'
}

def check_password(database, username, password):
    # This function checks if the password associated with the username
    # is correct. If it's not, this function returns False.
    # Else, it returns True.
    "***YOUR CODE HERE***"
    pass
```

If your function is written correctly, the following should occur:

```python
check_password(my_database, "Carl", "wrongpassword")
# Should return False
```

Calling the function with the above inputs should result in the function returning `False`.


```python
check_password(my_database, "Carl", "iamsuperman")
```
Calling the function with the above inputs should result in the function returning `True`.


**Exercise 2:** Write two functions: `encrypt()` and `decrypt()`. Each function takes in a string and a dictionary as an input. They should use the dictionary to either encrypt or decrypt the string.


EXAMPLE:

```python
encryption_code = {'a': 'b'}
encrypt('The password is apple.', encryption_code)
# The above should return  return 'The pbssword is bpple'


decryption_code = {'b': 'a'}
decrypt('The pbssword is bpple', decryption_code)
# The above should return 'The password is apple'
```

I've provided the starter code for you below:

```python
def encrypt(to_encrypt, encryption_code):
  "***YOUR CODE HERE***"
  pass

def decrypt(to_decrypt, decryption_code):
  "***YOUR CODE HERE***"
  pass
```