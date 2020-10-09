#!/usr/bin/python
#
# Name: Jojo Jaballas
# 
# Date: 10/8/2020
#
# Description: Simple script to demo use of function. To square a number.
#
def nsquared(n):
   return n**2

if __name__ == "__main__":
   n = int(input("Enter number: "))
   print(n,"^2 is ",nsquared(n),sep='')
