s=input()
s1=[]
s2=[]
ans=0
for i in range(len(s)):
    if(s[i]=="\\"):
        s1.append(i)
    elif(s[i]=="/" and s1):
        j = s1.pop()
        a=i-j
        ans+=a

        while(s2 and s2[-1][0]>j):
            a+=s2.pop()[1]
        s2.append([j,a])

print(ans)
print(len(s2),*(a for j, a in s2))