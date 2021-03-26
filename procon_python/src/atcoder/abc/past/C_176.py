n=int(input())
a=list(map(int,input().split()))
ans=0
tall=a[0]
for i in range(1,len(a)):
    if(tall < a[i]):
        tall=a[i]
    else:
        ans+=tall-a[i]
print(ans)