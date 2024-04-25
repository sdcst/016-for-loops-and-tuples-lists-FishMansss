#!python3 

"""
##### Task 1
Use a for loop to iterate through the list of numbers.
If the number is an even number print it out.
"""
import math
numbers = (3,19,3,6,3,6,7,8,5,4,6,78,0)
for i in numbers:
    if i % 2 == 0:
        print(i)
    