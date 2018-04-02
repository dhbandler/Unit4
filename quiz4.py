#Daniel Bandler
#4/2/18
#quiz4.py --- tanks my grade throughcompleting 4 functions

#Function 1:

x = int(input("Type a positive integer "))
def counting(x):
    if x >= 1:
        for i in range(1,x+1):
            print(i)
    else:
        print("I said positive integer. That was not a postive integer.")
counting(x)

#Function 2:

n = str(input("type a string here "))

def excitedPrint(n):
    print(n.upper(), "!!!")
excitedPrint(n)

#Function 3:

n = str(input("type a string here "))

def firstLetter(n):
    for ch in n:
        print(ch)
        break
firstLetter(n)

#Function 4:

x = input("Enter the first value here ")
y = input("Enter the second value here ")
z = input("Enter the third value here ")

def repeats(x,y,z):
    if x==y or x==z or y==z:
        return True
    else:
        return False
print(repeats(x,y,z))