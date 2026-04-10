#A31 Divisors

import sys
sys.stdin = open("input.txt","r")

N=int(input())

A=(N//3)+(N//5)-(N//15)

print(A)