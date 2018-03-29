#Daniel Bandler
#3/29/18
#warmup12.py -- finds GCF

def gcf(x,y):
        
    for i in range(x,0,-1):
        if x%i == 0 and y%i==0:
            return i

print(gcf(12,15))
print(gcf(5,9))
print(gcf(16,64))