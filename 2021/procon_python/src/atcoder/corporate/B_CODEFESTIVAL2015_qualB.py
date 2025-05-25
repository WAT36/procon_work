import collections
n,m=map(int,input().split())
a=list(map(int,input().split()))

n=len(a)//2

ans=0
listc=collections.Counter(a)
for k,v in listc.items():
    if(v>n):
        print(k)
        break
else:
    print("?")
