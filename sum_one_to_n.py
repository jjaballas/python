#!/usr/bin/python3.6
#
# Filename: sum_one_to_n.py
#
# Name: Jojo Jaballas
#
# Description: Python script to sum number from 1 to n.
#
# Date: 09/07/2020
# Version: 0.1

Nth_value=int(input("Enter nth number to sum up: "))
sum = 0
#for i in range(Nth_value+1):
#   sum += i
#print("Sum is ", sum)
i=1
while i <= Nth_value:
    sum += i
    i += 1
print("Sum of Nth value is: ", sum)
