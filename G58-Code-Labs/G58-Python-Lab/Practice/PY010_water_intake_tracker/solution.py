# Variable: daily water intake goal (in milliliters)
daily_goal = 3000

# Variables: water consumed during the day (in milliliters)
morning = 750
afternoon = 1000
evening = 500

# Processing: calculate total water consumed
total_water = morning + afternoon + evening

# Processing: calculate remaining water needed
remaining_water = daily_goal - total_water

# Output: display water intake summary
print("Daily Goal:", daily_goal, "ml")
print("Total Water Consumed:", total_water, "ml")
print("Remaining Water Needed:", remaining_water, "ml")

"""
Expected Output

Daily Goal: 3000 ml
Total Water Consumed: 2250 ml
Remaining Water Needed: 750 ml
"""