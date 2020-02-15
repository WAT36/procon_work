n,q=map(int,input().split())
a=[0 for _ in range(n+1)]
for _ in range(q):
    l,r,t=map(int,input().split())
    for i in range(l,r+1):
        a[i]=t
a.pop(0)
for i in range(len(a)):
    print(a[i])