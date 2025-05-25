s=input()
x='CODEFESTIVAL2016'
ans=0
for i in range(len(s)):
    if(s[i]!=x[i]):
        ans+=1
print(ans)