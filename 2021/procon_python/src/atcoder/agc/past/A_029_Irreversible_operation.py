s=input()

ans=0
b_count=0
for i in range(len(s)):
    if(s[i]=='W'):
        ans+=b_count
    else:
        b_count+=1
print(ans)