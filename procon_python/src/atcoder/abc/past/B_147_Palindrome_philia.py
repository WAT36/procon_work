s=input()
ans=0
for i in range(len(s)):
    j=len(s)-1-i
    if(i >= len(s)-1-i):
        break
    elif(s[i] != s[j]):
        ans+=1
print(ans)