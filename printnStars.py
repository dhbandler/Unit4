#Daniel Bandler
#3/19/18
#printnStars.py - prints n layers of stars
n = int(input("How many rows? "))

def stars(n):
    for i in range(1,n+1):
        print("*"*i)

print(stars(n))