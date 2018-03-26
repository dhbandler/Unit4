#Daniel Bandler
#3/26/18
#warmup11.py returns true if num is prime, otherwise false
#ex. print(prime(9)) == false

def prime(num):
    for i in range(2,num):
        if num%i == 0:
            return False
    return True   

        
print(prime(9))
print(prime(10))
print(prime(11))

