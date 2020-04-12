k=int(input())
ans=0

gcd_ans=[[-1 for i in range(k+1)] for _ in range(k+1)]

def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b, a%b)

def gcd_lookup(i,j):
    if(gcd_ans[i][j]==-1):
        gcd_ans[i][j]=gcd(i,j)
        gcd_ans[j][i]=gcd_ans[i][j]
    return gcd_ans[i][j]

for i in range(1,k+1):
    for j in range(i,k+1):
        for l in range(j,k+1):
            if(i==j and j==l):
                ans+=gcd_lookup(gcd_lookup(i,j),l)
            elif((i==j) or (j==l) or (l==i)):
                ans+= 3*(gcd_lookup(gcd_lookup(i,j),l))
            else:
                ans+= 6*(gcd_lookup(gcd_lookup(i,j),l))

print(ans)
