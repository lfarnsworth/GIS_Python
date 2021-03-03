# 2. List overlap
# Using these lists:
#
# list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
# list_b = ['dog', 'hamster', 'snake']
# Determine which items are present in both lists.
# Determine which items do not overlap in the lists.

# #Determine which items overlap in the lists:
def intersection(list_a, list_b):
    list_c =[str for str in list_a if str in list_b]
    return list_c

list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
list_b = ['dog', 'hamster', 'snake']

print('These are in common:')
print(intersection(list_a, list_b))
print('\r\n')

#Determine which items DO NOT overlap in the lists:

list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
list_b = ['dog', 'hamster', 'snake']

def exclusion(list_a, list_b):
    list_c =[str for str in list_a if not str in list_b]
    list_c.extend([str for str in list_b if not str in list_a])
    return list_c

print('These are NOT in common:')
print(exclusion(list_a, list_b))
print('\r\n')

# Feedback - Great! Thanks for the helpful print statement in common/not in common. Keep an eye on how you are laying
# out your code to keep it clean and organized.