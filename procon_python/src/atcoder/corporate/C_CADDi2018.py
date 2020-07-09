n,p=map(int,input().split())

#xの約数を列挙する
def divisor(x):
    ans=set([])
    i=1
    while(i*i<=x):
        if(x%i==0):
            ans.add(i)
            ans.add(x//i)
        i+=1
    ans=sorted(list(ans))
    return ans


#xの素因数分解
def prime_factorization(x):
    ans={}
    divisors=divisor(x)
    xi=x
    for di in divisors:
        if(xi==1):
            break
        elif(di<=1):
            continue
        else:
            dj=0
            while(xi%di==0 and xi!=1):
                xi//=di
                dj+=1
            if(dj>0):
                ans[di]=dj
    return ans

pf=prime_factorization(p)
#print(pf)
ans=1
for k,v in pf.items():
    if(v>=n):
        ans*=(k**(v//n))
print(ans)
