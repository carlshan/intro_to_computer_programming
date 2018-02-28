"""
This file shows you how you can open and save files.
Please also use this website as a guide: https://www.programiz.com/python-programming/file-operation

If you have a file on your desktop called 'hello.txt', the code below will
open it up and print the contents inside.

We're going to use the `open()` function.

It takes in two arguments:
    filename: this is a string that describes the file you want to open

    method: this is a string that has to be 'r', 'w' or 'a'
        'r' - 'read': this will allow you to open and read the contents of the file
        'w' - 'write': this allows you to overwrite the file
        'a' - 'append': this allows you to append stuff to the end of the file
        See this link for more options: https://www.programiz.com/python-programming/file-operation

After you open a file, you can use the .read() or .readlines() methods to get the contents from it.

You can also use .write() and .writelines() to add additional lines to the file.

After you're done with all that, use the .close() method to close the connection.

The code below demonstrates some of this.

"""

# OPENING AN EXISTING FILE
# This will open the 'hello.txt' file for 'reading' plus 'writing' and assign it to the variable my_file
my_file = open('/Users/cshan/Desktop/hello.txt', 'r+w')

# This stores all the lines into a giant string
all_the_lines = my_file.readlines()
for line in all_the_lines:
    print(line)

# Writing a single string at the end of a file.
my_file.write("Hello!")

# Writing multiple lines
to_write = ['try this ', 'and this']
my_file.writelines(to_write)

# Make sure you close the connection to give the resources taken by this operation back to your computer
my_file.close()
