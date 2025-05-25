import math
n=int(input())
if(n==1):
    print("BOWWOW")
else:
    n=n*(1+n)//2
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            print("BOWWOW")
            break
    else:
        print("WANWAN")
