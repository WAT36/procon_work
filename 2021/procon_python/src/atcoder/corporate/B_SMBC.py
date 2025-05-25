import math
n=int(input())
if(n%1.08==0):
    print(int(n/1.08))
else:
    x=n/1.08
    n_low=int(math.floor(1.08*math.floor(x)))
    n_high=int(math.floor(1.08*math.ceil(x)))
    if(n==n_low):
        print(int(math.floor(x)))
    elif(n==n_high):
        print(int(math.ceil(x)))
    else:
        print(":(")