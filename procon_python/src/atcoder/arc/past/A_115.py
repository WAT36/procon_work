n,m=map(int,input().split())
s=[]
odds=0
evens=0
for i in range(n):
    si=list(input())
    if(si.count('1')%2==0):
        evens+=1
    else:
        odds+=1
print(odds*evens)

