#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = str(number)[-1]
if number < 0:
    str1 = -1 * int(str1)
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, str1))
else:
    if int(str1) > 5:
        print(f"Last digit of {number} is {str1} and is greater than 5")
    elif int(str1) == 0:
        print(f"Last digit of {number} is {str1} and is 0")
    else:
        print(f"Last digit of {number} is {str1} and is less than 6 and not 0")