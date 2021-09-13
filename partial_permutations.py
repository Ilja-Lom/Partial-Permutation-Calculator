'''
Author: Ilja Lom...
GitHub: https://github.com/Ilja-Lom
Publication-Date: 13/09/2021
Description: 
    An algorithm to find the total number of partial permutations that can be formed 'k' number of objects in an 'n' number collection
    Given positive integers of n, and k, return the total number of partial permutations.
'''

#Take user inputs
n =int(input("---Enter n:---\n---")) #Total number of objects in collection
k = int(input("---Enter k:---\n---")) #Number of ordering objects

#Factorial processing
def factorial(n, k):
    fact = 1
    for i in range(n-k):
        fact *= (i + 1)
    return(fact)

#Calculating number of partial permutations
def permutation(n, k):
    permutation = int(factorial(n,0)/factorial(n,k) % 1000000)
    return(permutation)

#Calling the  class, and printing value
print(permutation(n, k)) #Forwarding the 'n', and 'k' variables to the 'permutation' class













