bank = {}
# This is how you make an empty dictionary.
# Note that it uses curly braces rather than square braces like a list.

bank = {'carl': 1000}
# You add values to the bank using pairs of items separated by a colon :
# The right side is called the 'key'. It's like the account number of someone
# in the bank.
# The right side is know as the 'value'.

bank = {'carl': 1000, 'A': 0, 'B': 100}
# You separate pairs of items using the comma, just like with lists.
# Add 4 students, giving them all different amounts.

bank['carl']
# this is how you access the value, using the key

bank['A'] = bank['A'] + 1000
# this is how you modify a value

del bank['A']
# this is how you delete a values

bank = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

for account in bank:
    print(account)


# using a for-loop with a dictionary will loop over the KEYS of the dictionary.
