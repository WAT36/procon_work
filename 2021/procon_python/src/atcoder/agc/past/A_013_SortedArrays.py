n=int(input())
a=list(map(int,input().split()))
up=False
down=False
ans=0
for i in range(n-1):
    if(not up and not down):
        if(a[i]<a[i+1]):
            up=True
        elif(a[i]>a[i+1]):
            down=True
    elif(up):
        if(a[i]>a[i+1]):
            ans+=1
            up=False
    elif(down):
        if(a[i]<a[i+1]):
            ans+=1
            down=False
ans+=1
print(ans)