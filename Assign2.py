"""

Ricardo Veras
Student #: 250692934
CompSci-1026A Assignment 2 (Assign2 file)

This file will call functions from file code_check to check whether a users string input of numbers
    is a valid basic, positional or UPC code.
It will then add each valid code to its corresponding list that will begin as an empty list.
If no codes are in a list, the output of that list will be 'None'.
If an input does not fit into any list, it will be added to the list none_list.
Each list will then be joined into a new string containing each code, separated by commas.

A summary will then be outputted, displaying the type of each list followed by its corresponding list

"""

from code_check import basic, positional, upc   # import functions from file code_check.py

basic_list = []
positional_list = []
upc_list = []
none_list = []                                  # list containing codes that do not fit in any other code category
user = input('Please enter code (digits only) (enter 0 to quit): ')

while user != '0':                              # while users input is not 0, call functions to check if the users input is a valid basic, positional or UPC code
    if basic(user) is True:
        basic_list.append(user)
    if positional(user) is True:
        positional_list.append(user)
    if upc(user) is True:
        upc_list.append(user)
    if basic(user) is False and positional(user) is False and upc(user) is False:    # if code is not basic, positional or UPC, add to list none_list
        none_list.append(user)
    user = input('Please enter another code (digits only) (enter 0 to quit): ')


if len(basic_list) == 0:                        # if no codes are in a list, output None instead of an empty list
    basic_list.append('None')
if len(positional_list) == 0:
    positional_list.append('None')
if len(upc_list) == 0:
    upc_list.append('None')
if len(none_list) == 0:
    none_list.append('None')


basic_list = ', '.join(basic_list)             # Combining list into string of each code, separated by commas
positional_list = ', '.join(positional_list)
upc_list = ', '.join(upc_list)
none_list = ', '.join(none_list)


print('\nSummary\nBasic: {}\nPosition: {}\nUPC: {}\nNone: {}'.format(basic_list, positional_list, upc_list, none_list))
