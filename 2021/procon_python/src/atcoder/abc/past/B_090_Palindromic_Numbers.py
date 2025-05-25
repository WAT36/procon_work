a,b=map(int,input().split())
ans=0
for i in range(a,b+1):
    rev_i=''.join(list(reversed(list(str(i)))))
    if(str(i)==rev_i):
        ans+=1
print(ans)