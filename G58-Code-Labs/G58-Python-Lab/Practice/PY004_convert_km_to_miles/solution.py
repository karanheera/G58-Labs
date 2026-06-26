# Input: user enters distance in kilometers (string)
km_input = input("Enter distance in kilometers: ")

# Concept: input() always returns text (string)

# Type Conversion: convert text into number (float)
km = float(km_input)

# Processing: convert km to miles
miles = km * 0.621371

# Output: display result
print("Miles:", miles)


"""
Expected Output: 
Enter distance in kilometers: (Let's say user inputs 10)
Miles: 6.21371

"""