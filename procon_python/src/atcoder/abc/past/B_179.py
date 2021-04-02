n=int(input())
ans=0
ansi=0
for i in range(n):
    d1,d2=map(int,input().split())
    if(d1==d2):
        ansi+=1
    else:
        ans=max(ans,ansi)
        ansi=0
else:
    ans=max(ans,ansi)

if(ans>=3):
    print('Yes')
else:
    print('No')