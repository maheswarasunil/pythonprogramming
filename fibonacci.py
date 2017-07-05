#!/usr/bin/python

#
# Program to print first 20 numbers in fibonacci
#

length_count = 20
fibonacci_array = [i for i in range(length_count)]

def get_fibonacci(n):
    return fibonacci_array[n-1] + fibonacci_array[n-2]

for i in range(length_count):
    if i == 0:
        fibonacci_array[0] = 0
    elif i == 1:
        fibonacci_array[1] = 1
    else:
        fibonacci_array[i] = get_fibonacci(i)

print fibonacci_array