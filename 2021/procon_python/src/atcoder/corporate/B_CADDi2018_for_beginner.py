n,h,w=map(int,input().split())
ans=0
for i in range(n):
    a,b=map(int,input().split())
    if(h<=a and w<=b):
        ans+=1
print(ans)