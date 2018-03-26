#Daniel
#3/26/18
#countdownn.py counts down from integer
n = int(input("Enter a number "))

def countdown(n):
    i = n
    while i > 0:
        print(i)
        i -= 1
        if i == 0:
            print("BOOM")
countdown(n)
