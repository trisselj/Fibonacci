# Author: Jake Trissel
# Github Username: trisselj
# Date: 07/17/2024
# Description: Returns the requested number in the fibonacci sequence

#Defining our initial function for which we will use (Assuming no unexpected inputs)
def fib(n):
    a, b =1, 1 #Definig the first two numbers in the sequence
    for _ in range(2, n): #Loop for calculating Fibonacci sequence up to nth integer
        a, b = b, a + b
    if n > 1:
        return b
    else:
        return a
    
print(fib(10))