# Given string:
string = 'hi dee hi how are you mr dee'

# Convert string to list:
List_string = string.split()
# print(List_string)

# code snippet from: https://www.geeksforgeeks.org/python-get-unique-values-list/
def unique(list1):
    # intilize a null list
    unique_list = []
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    # print list
    # for x in unique_list:
    #     print(x)
    return unique_list
# end code snippet

# Get unique values of string list
unique_string_list = unique(List_string)
# print(unique_string_list)

# step through uniques, count them in original string and print result
for item in unique_string_list:
    item_word_count = List_string.count(item)
    if item_word_count > 1:
        print(item + ': ' + str(item_word_count) + ' counts')
    else:
        print(item + ': ' + str(item_word_count) + ' count')

# Feedback - Good jhob, looks a bit neater than previous challenges, I made one tweak to help with the (s) print.
# if there are things that you don't need any more, clean up your code by deleting out the commented out parts.