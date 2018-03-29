#Daniel Bandler
#3/29/18
#warmup12.py -- finds GCF

def gcf(x,y):
    if x%y == 0:
        return y
        
    for i in range(int(x/2,1), 0, -1):
        if x%i == 0 and y%i==0:
            gcf = i
            break
    return i
gcf(12,15)