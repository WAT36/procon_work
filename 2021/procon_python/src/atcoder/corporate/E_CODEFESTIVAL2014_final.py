n=int(input())
r=list(map(int,input().split()))

ans=0
upflag=False
downflag=False
for i in range(len(r)-1):
    if(upflag):
        if(r[i]>r[i+1]):
            ans+=1
            upflag=False
            downflag=True
    elif(downflag):
        if(r[i]<r[i+1]):
            ans+=1
            upflag=True
            downflag=False
    else:
        if(r[i]>r[i+1]):
            ans+=1
            upflag=False
            downflag=True
        elif(r[i]<r[i+1]):
            ans+=1
            upflag=True
            downflag=False
else:
    ans+=1

if(ans>=3):
    print(ans)
else:
    print(0)