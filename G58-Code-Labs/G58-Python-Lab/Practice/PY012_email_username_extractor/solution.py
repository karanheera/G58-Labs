# Python program to extract username from email address
email = "john.smith@gmail.com"

# find position of '@'
at_pos = email.index("@")

# extract username using slicing
username = email[:at_pos]

# display output
print("Email:", email)
print("Username:", username)
print("Index of '@' in this email is:", at_pos)

"""
Expected Output

Email: john.smith@gmail.com

Username: john.smith
Index of '@' in this email is: 10
"""