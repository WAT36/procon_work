n=int(input())
s=input()
ans=1
precolor=s[0]
for i in range(n):
    if(precolor != s[i]):
        ans+=1
    precolor =s[i]
print(ans)