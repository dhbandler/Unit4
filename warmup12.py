#Daniel Bandler
#3/29/18
#warmup12.py -- finds GCF

def gcf(x,y):
    if x%y == 0:
        return y
        
    for i in range(1,x/2):
        if x%i == 0 and y%i==0:
            return i
gcf(12,15)