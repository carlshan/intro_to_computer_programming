# Dictionary Assignments
By Carl Shan

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


**Exercise 3:** Write a function called `reverse_dictionary()` that takes a dictionary as input, and returns a new dictionary with the `key` and `values` reversed.

Example:

```python
a = {'carl': 5, 'billy': 2, 'yeet': 'feet'}

new_a = reverse_dictionary(a)

print(new_a)
# the above should print
# {2: 'billy', 5: 'carl', 'feet': 'yeet'}
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

**Exercise 3:** The goal of this exercise is to create a gradebook. It is from [Erle Robotics](http://erlerobot.com/).

First, create three dictionaries: `lloyd`, `alice`, and `tyler`. They should look like the below:

```python
lloyd = {
  "name": "Lloyd",
  "homework": [90.0,97.0,75.0,92.0],
  "quizzes": [88.0,40.0,94.0],
  "tests": [75.0,90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}
```

How do the following:

1. Create a function named `average()` that takes a list of numbers as input, and returns the average of that list.
2. Create a function called `calculate_grade()` that takes a student dictionary as input and returns the weighted average, where the weights are applied in the following manner:
    * Quizzes: 30%
    * Tests: 60%
    * Homework: 10%

An example of this is below:

```python
calculate_grade(lloyd)
# it should print 
# 80.549

calculate_grade(alice)
# 91.149

calculate_grade(tyler)
# 79.899
```

3. Create a new function called `get_letter_grade()` that takes a number as an input, and returns the corresponding letter grade according to the scheme below:

```
If score is 90 or above: return "A"
Else if score is 80 or above: return "B"
Else if score is 70 or above: return "C"
Else if score is 60 or above: return "D"
Otherwise: return "F"
```

4. Define a function called `get_class_average()` that takes in a list of students as input, and returns the average score (e.g., out of 100) of the students in the class.