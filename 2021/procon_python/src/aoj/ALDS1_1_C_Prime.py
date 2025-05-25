import math
def isPrime(x):
    if(x<2):
        return False
    else:
        for i in range(2,int(math.sqrt(x)//1)+1):
            if(x%i==0):
                return False
        return True

n=int(input())
ans=0
for i in range(n):
    a=int(input())
    if(isPrime(a)):
        ans+=1
print(ans)
