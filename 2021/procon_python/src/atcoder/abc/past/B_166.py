n,k=map(int,input().split())
ans=set([i for i in range(1,n+1)])

for i in range(k):
    d=int(input())
    a=set(list(map(int,input().split())))
    ans=ans - a
print(len(ans))