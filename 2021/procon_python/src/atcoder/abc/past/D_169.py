n=int(input())

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

div_n=divisor(n)[1:]
#print(div_n)

prime_n=[]
isprime=[True for _ in range(len(div_n))]
for i in range(len(div_n)):
    if(isprime[i]):
        for j in range(i+1,len(div_n)):
            if(div_n[j]%div_n[i]==0):
                isprime[j]=False
        prime_n.append(div_n[i])
    else:
        pass
#print(prime_n)

soinsu={}
for di in prime_n:
    ans_di=0
    ni=n
    while(ni%di==0):
        ni//=di
        ans_di+=1
    soinsu[di]=ans_di
#print(soinsu)

ans=0
for k,v in soinsu.items():
    vi=v
    i=1
    while(vi>=i):
        vi-=i
        i+=1
        ans+=1
print(ans)
