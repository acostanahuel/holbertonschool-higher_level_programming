#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of"
lasts = number % 10
if lasts > 5:
    print(f"{str} {number} is {lasts} and is greater than 5\n")
elif lasts == 0:
    print(f"{str} {number} is {lasts} and is 0\n")
elif lasts < 6 and lasts != 0:
    print(f"{str} {number} is {lasts} and is less than 6 and not 0\n")