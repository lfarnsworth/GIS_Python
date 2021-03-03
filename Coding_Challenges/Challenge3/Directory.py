# load library for file operations in os
import os
# Set our base path
path = 'C:\coding_challenge3'
# build/test the directory structure
if not os.path.exists(path):
    os.mkdir(path)
if not os.path.exists(path + '\site'):
    os.mkdir(path + '\site')
if not os.path.exists(path + '\draft_code'):
    os.mkdir(path + '\draft_code')
if not os.path.exists(path + '\draft_code\pending'):
    os.mkdir(path + '\draft_code\pending')
if not os.path.exists(path + '\draft_code\complete'):
    os.mkdir(path + '\draft_code\complete')
if not os.path.exists(path + '\includes'):
    os.mkdir(path + '\includes')
if not os.path.exists(path + '\layouts'):
    os.mkdir(path + '\layouts')
if not os.path.exists(path + '\layouts\default'):
    os.mkdir(path + '\layouts\default')
if not os.path.exists(path + '\layouts\post'):
    os.mkdir(path + '\layouts\post')
if not os.path.exists(path + '\layouts\post\posted'):
    os.mkdir(path + '\layouts\post\posted')

# look for empty folders and delete them
# if not empty, recall the function and walk again
def delete_recursively(func_path):
    list_path = os.listdir(func_path)
    print(func_path)
    print(list_path)
    if not list_path:
        print('IT WAS EMPTY!')
        print('LETS DELETE!')
        os.rmdir(func_path)
    else:
        print('I GUESS ITS NOT EMPTY')
        for items in list_path:
            delete_recursively(func_path + '\\' + items)
        delete_recursively(func_path)
    print('\r\n')
    return 0
# call the function
delete_recursively(path)


# Feedback - Good work, quite verbose with all the mkdir but worked fine. I do suggest using a standard file naming
# convention for your files, Task_1.py for example to make it easier.