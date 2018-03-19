#Daniel Bandler
#3/19/18
#returnDemo.py - how to use return

from random import randint

def randEven(low,high):
    n = randint(low,high)
    while n%2 != 0:
        n = randint(low,high)
    print(n)
    
    
randEven(11,11) #test of randEven
