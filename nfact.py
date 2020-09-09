#!/usr/bin/python3.8
#
# Filename: nfact.py
#
# Name: Jojo Jaballas
#
# Description: Python script to calculated the factorial of a number.
#
# Date: 09/09/2020
# Version: 0.1
import sys

n=int(sys.argv[1])
nfact = 1
j = n
i = 1
while i <= j:
   #print(n,"\t",i,"\t",nfact)
   nfact = nfact * n
   n -= 1
   i += 1
print(j,"! is ",nfact,sep='')
