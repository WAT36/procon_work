n,l=map(int,input().split())
s=input()
count=1
ans=0
for i in range(n):
    if(s[i]=='+'):
        count+=1
    else:
        count-=1
    if(count>l):
        ans+=1
        count=1
print(ans)