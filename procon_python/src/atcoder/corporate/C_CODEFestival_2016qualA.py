s=input()
k=int(input())

alpha=list('abcdefghijklmnopqrstuvwxyz')

ans=[]
for i in range(len(s)):
    ki= 26-alpha.index(s[i]) if s[i]!='a' else 0
#    print(ki,k)
    if(i==len(s)-1):
        kn=k+alpha.index(s[i])
        kn=kn%26
        ans.append(alpha[kn])
    elif(ki<=k):
        ans.append('a')
        k-=ki
    else:
        ans.append(s[i])
print(''.join(ans))