# Bad Password Generator
# Takes 3 arguments (Name, Street, Birth year) and generates awful password
# Load library to get command-line arguments and select random value
import sys
import random

street_name = sys.argv[1]
birth_year = sys.argv[2]
first_name = sys.argv[3]

special_char = random.choice('`~!@#$%^&*()_+')
print('This is your terrible password: ')
print(street_name[:3] + birth_year[-2:] + first_name[::-1] + special_char)

#Feedback - Ah this is awesome! Made me laugh, but I think those passwords are better than most! Well done!