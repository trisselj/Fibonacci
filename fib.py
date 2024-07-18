# Author: Jake Trissel
# Github Username: trisselj
# Date: 07/17/2024
# Description: Returns the requested number in the fibonacci sequence

#Defining our initial function for which we will use (Assuming no unexpected inputs)
def fib(n):
    a, b =1, 1 #Definig the first two numbers in the sequence
    for _ in range(2, n): #Loop for calculating Fibonacci sequence up to nth integer
        temporary = a #Storing a as a temprorary integer
        a = b #Making a to be b
        b = temporary + b #Updating b to be the original value of a in addition to b
    if n > 1: #Makes code read as our final value so long as n is > 1 otherwise it will just read as a
        return b
    else:
        return a