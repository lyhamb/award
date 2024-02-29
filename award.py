""" Task #4 -  Logical Programming - Operators """

""" 
The goal of this project is to output an award description based on the times
inputted by the user.
"""

# Request completion time for each event from the user
time1 = float(input("Time taken in minutes to complete the swimming event: "))
time2 = float(input("Time taken in minutes to complete the cycling event: "))
time3 = float(input("Time taken in minutes to complete the running event: "))

# Calculate total triathlon time
triathlon_time = time1 + time2 + time3

# Output the total time
print(f"The total time taken was {triathlon_time} minutes.")

# Calculate the award given
if triathlon_time <= 100:
    award = "Provincial Colours"
elif triathlon_time <= 105:
    award = "Provincial Half Colours"
elif triathlon_time <= 110:
    award = "Provincial Scroll"
else:
    award = "No Award"

# Display award given
print(f"Result: {award}")