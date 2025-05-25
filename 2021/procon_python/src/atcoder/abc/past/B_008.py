n=int(input())
s={}
max_v=0
ans=""
for i in range(n):
    si=input()
    v=s.get(si, 0)+1
    s[si]=v
    if(max_v<v):
        max_v=v
        ans=si
print(ans)
