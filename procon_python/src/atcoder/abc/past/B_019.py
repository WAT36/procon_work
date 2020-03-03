s=input()
ans=""
w=s[0]
count=0
for i in range(len(s)):
    if(w != s[i]):
        ans+=w+str(count)
        w=s[i]
        count=1
    else:
        count+=1
else:
    ans+=w+str(count)
print(ans)