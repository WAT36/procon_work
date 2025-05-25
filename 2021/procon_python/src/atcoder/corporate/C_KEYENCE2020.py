n,k,s=map(int,input().split())
ans=[]
i=0
if(s!=10**9):
    for _ in range(n):
        if(i<k):
            ans.append(s)
            i+=1
        else:
            ans.append(10**9)
else:
    for _ in range(n):
        if(i<k):
            ans.append(s)
            i+=1
        else:
            ans.append(1)

print(*ans)
