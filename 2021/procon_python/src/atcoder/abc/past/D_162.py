n=int(input())
s=input()

r=list(s).count('R')
g=list(s).count('G')
b=list(s).count('B')

ans=r*g*b
for i in range(n):
    for j in range(i+1,n):
        k=j+(j-i)
        if(k<n and s[i]!=s[j] and s[j]!=s[k] and s[k]!=s[i]):
#            print(i,j,k)
            ans-=1
print(ans)
