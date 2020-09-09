#!/usr/bin/python3.6
#
# Filename: nfact.py
#
# Usage: nfact.py some_number
#
# Name: Jojo Jaballas
#
# Description: Python script to calculated the factorial of a number.
#
# Date: 09/09/2020
# Version: 0.2 Updated with function.

import sys

n=int(sys.argv[1])

def nfactorial(n):
   j = n
   i = 1
   nfact = 1
   while i <= j:
       nfact = nfact * n
       n = n - 1
       i = i + 1
   return nfact

if __name__ == "__main__":
   print(n,"! is ",nfactorial(n),sep='')

