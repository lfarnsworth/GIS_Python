# #Determine which items overlap in the lists:
def intersection(list_a, list_b):
    list_c =[str for str in list_a if str in list_b]
    return list_c


list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
list_b = ['dog', 'hamster', 'snake']
print('these are in common:')
print(intersection(list_a, list_b))
print('\r\n')

#Determine which items DO NOT overlap in the lists:

list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
list_b = ['dog', 'hamster', 'snake']
def intersection(list_a, list_b):
    list_c =[str for str in list_a if not str in list_b]
    list_c.extend([str for str in list_b if not str in list_a])
    return list_c
print('These are NOT in common:')
print(intersection(list_a, list_b))
print('\r\n')
