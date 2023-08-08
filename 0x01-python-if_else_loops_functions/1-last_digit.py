#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if number < 0:
    last_digit = -last_digit

if last_digit > 5:
    num_is = "and is greater than 5"
elif last_digit == 0:
    num_is = "and is 0"
else:
    num_is = "and is less than 6 and not 0"

if number < 0:
    print("Last digit of", number, "is", last_digit, num_is)
else:
    print("Last digit of", number, "is", last_digit, num_is)
