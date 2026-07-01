# Python program to display character indexes while ignoring whitespace

# Given string
text = "Karan Heera"

# This variable keeps track of the index of
# only the visible (non-whitespace) characters.
visible_index = 0


# First loop: Print the indexes

for char in text:

    # Check whether the current character is NOT whitespace.
    # Spaces, tabs, and newlines are ignored.
    if not char.isspace():

        # Print the current visible index.
        # end=" " keeps printing on the same line.
        print(visible_index, end=" ")

        # Increase the visible index for the next character.
        visible_index += 1

# Move the cursor to the next line.
print()


# Second loop: Print the characters

for char in text:

    # Ignore whitespace characters.
    if not char.isspace():

        # Print the visible character.
        # end=" " keeps printing on the same line.
        print(char, end=" ")

"""
Expected Output

0 1 2 3 4 5 6 7 8 9 
K a r a n H e e r a 

"""