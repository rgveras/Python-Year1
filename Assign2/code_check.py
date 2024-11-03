"""

Ricardo Veras
Student #: 250692934
CompSci-1026A Assignment 2 (code_check file)


This file, code_check.py will be utilized with Assign2.py

This file includes the functions that Assign2.py will call to check whether a string of numbers
as input is a valid basic code, positional code, or UPC code.

It contains 3 functions, one for each type of code, returning True if the input is a valid code or False if not valid.

"""


def basic(x):                           # function to determine if x is a valid basic code
    bin = 0                             # bin = base identification number
    i = 0
    for i in x:
        bin += int(i)
    bin -= int(i[-1])                   # sum of base identification digits minus last digit
    result = bin % 10
    if str(result) == x[-1]:            # if the result is equal to last digit in x
        flag = True
    else:
        flag = False
    return flag                         # True if x is a basic code, False otherwise


def positional(x):                      # function to determine if x is a valid positional code
    bin = 0
    count = 0
    while count < (len(x) - 1):
        bin += ((count + 1) * int(x[count]))    # digits position in the string multiplied by integer value of that digit
        count += 1
    result = bin % 10
    if str(result) == x[-1]:
        flag = True
    else:
        flag = False
    return flag                         # True if x is positional code, False otherwise


def upc(x):                             # function to determine if x is a valid UPC code
    bin = 0
    count = 0
    while count < (len(x)-1):
        if count % 2 == 0:              # if odd digit of x, multiply integer value of that digit by 3 (modulo 2 will be zero since digit 1 is at position 0)
            bin += (int(x[count]) * 3)
            count += 1
        else:                           # if even digit of x, use value of that digits integer
            bin += int(x[count])        # bin = sum of odd digits multiplied by 3 and even digits values
            count += 1
    result = bin % 10                   # result = remainder when divided by 10 to get number between 1 and 10
    if result != 0:
        result = 10 - result            # if result is not 0, subtract result from 10
    if str(result) == x[-1]:
        flag = True
    else:
        flag = False
    return flag                         # True if x is UPC code, False otherwise
