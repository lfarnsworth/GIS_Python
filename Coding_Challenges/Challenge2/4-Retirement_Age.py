#Ask a person their name and store it to variable "age_str".
age_str = input("What is your age? ")

# Convert age to integer
age_int = int(age_str)

# calculate years from retirement
retirement_int = 65 - age_int

# print the retirement age
print("You are " + str(retirement_int) + " year(s) from retirement.")
