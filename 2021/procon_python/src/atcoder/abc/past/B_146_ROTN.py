n=int(input())
s=input()
alpha=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
ans=""
for i in range(len(s)):
    si=s[i]
    si_ind=alpha.index(si)
    si_ind+=n
    if(si_ind>=len(alpha)):
        si_ind-=len(alpha)
    ans+=alpha[si_ind]
print(ans)
