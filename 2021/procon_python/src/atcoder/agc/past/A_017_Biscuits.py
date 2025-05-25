n,p=map(int,input().split())
a=list(map(int,input().split()))
even=len([a[i] for i in range(len(a)) if a[i]%2==0])
odd=len([a[i] for i in range(len(a)) if a[i]%2!=0])

def make_c(n):
    nck=[1]
    child=n
    mother=1
    for i in range(1,n+1):
        nck.append(nck[i-1]*child//mother)
        child-=1
        mother+=1
    return nck



if(p==0):
    comb=make_c(odd)
    comb=comb[0::2]
    odd_comb=sum(comb)
    ans=(2**even)*odd_comb
else:
    comb=make_c(odd)
    comb=comb[1::2]
    odd_comb=sum(comb)
    ans=(2**even)*odd_comb
print(ans)
