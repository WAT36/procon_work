n=int(input())
a=[]
ans=0
for i in range(n):
    a.append(int(input()))
    if(i>0 and a[-2]==1 and a[-1]>0):
        ans+=1
        a[-2]-=1
        a[-1]-=1
    ans+=a[-1]//2
    a[-1]=a[-1]%2
    if(i>0 and a[-2]==1 and a[-1]==1):
        ans+=1
        a[-2]-=1
        a[-1]-=1

print(ans)
