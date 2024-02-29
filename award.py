""" Task #4 -  Logical Programming - Operators """

""" 
The goal of this project is to output an award description based on the times
inputted by the user.
"""

# Data validation function
def get_valid_number():
    while True:
        user_input = input(f"Please enter the {input_text}")
        try:
            user_float = float(user_input)
            if user_float > 0:
                return user_float
            elif user_float <= 0:
                print ("Enter a number greater than 0.")
        except ValueError:
            print("Enter a valid number.")

# Request completion time for each event from the user
input_text = "time taken in minutes to complete the swimming event: "
time1 = get_valid_number()
input_text = "time taken in minutes to complete the cycling event: "
time2 = get_valid_number()
input_text = "time taken in minutes to complete the running event: "
time3 = get_valid_number()

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