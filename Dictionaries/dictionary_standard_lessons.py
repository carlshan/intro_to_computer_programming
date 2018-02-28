# ======================
# | STANDARD EXERCISES |
# ======================

# EXERCISE 1
# Standard Exercise 1 - Creating a dictionary
# First, create an empty dictionary
# Then, add a key-value pair to it. Have the key be 'my_favorite_class'
# and the value be the name of your favorite Nueva class.


# Standard Exercise 2 - Adding to a dictionary
# Create a function that takes a dictionary as input. (It could be the one you created
# in the last problem).
# This function should add 2 to each input.

""" EXAMPLE
my_dict = {'carl': 100, 'justin_bieber': 5}
change_dictionary(my_dict)

print(my_dict)

> {'carl': 102, 'justin_bieber': 7}

"""

def change_dictionary(dictionary):
  "***Your Code Here!***"
  # Hint: You should loop over the dictionary
  pass # Delete this line when you write your own code


# Exercise 3
# Create a function that takes two inputs: a list and a dictionary
# This function should modify the dictionary so that it counts the number
# of times a pokemon was captured.
# I've provided the list and dictionary for you below.

""" EXAMPLE
pokemon_zoo = {'pikachu': 0, 'blastoise': 1}
captured_pokemon = ['pikachu', 'pikachu', 'blastoise']
update_pokemon_zoo(pokemon_zoo, captured_pokemon)

print(pokemon_zoo)
pokemon_zoo = {'pikachu': 2, 'blastoise': 2}

"""

# This is all the Pokemon you've captured.
captured_pokemon = ['magikarp', 'mankey', 'pikachu', 'voltorb', 'mankey',
                    'venomoth','weedle', 'weedle', 'magikarp', 'kakuna']

# Here is a dictionary that describes each Pokemon and how many of each
# type you've captured.
# You don't have any Pokemon, so your zoo is empty.
pokemon_zoo = {'kakuna': 0,
               'magikarp': 0,
               'mankey': 0,
               'pikachu': 0,
               'venomoth': 0,
               'voltorb': 0,
               'weedle': 0}

# Write a function that changes pokemon_zoo to reflect the new
def update_pokemon_zoo(zoo, captured):
  "***Your Code Here!***"
  pass # Delete this line after you write your own code

# =======================
# | Challenge Exercises |
# =======================

# Challenge Exercise 1
# Write a function that checks if a password corresponds to a username in a
# database.
# It should return False if not, and True if the password is correct.

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


# Challenge Exercise 2
# Write two functions: encrypt and decrypt
# They should each take a string and dictionary and encrypt the string using the
# dictionary

"""EXAMPLE:

encryption_code = {'a': 'b'}
encrypt('He is a monkey.', encryption_code)
> 'He is b monkey.'


decryption_code = {'b': 'a'}
decrypt('He is b monkey.', decryption_code)
> 'He is a monkey.'

"""

def encrypt(to_encrypt, encryption_code):
  "***YOUR CODE HERE***"
  pass

def decrypt(to_decrypt, decryption_code):
  "***YOUR CODE HERE***"
  pass
