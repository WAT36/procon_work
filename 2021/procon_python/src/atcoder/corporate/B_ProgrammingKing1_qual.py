n,k=map(int,input().split())
a=list(map(int,input().split()))
l=[0 for _ in range(len(a))]
r=[0 for _ in range(len(a))]
MOD=(10**9)+7

for i in range(len(a)):
    for j in range(len(a)):
        if(j<i and a[j]<a[i]):
            l[i]+=1
        elif(i<j and a[i]>a[j]):
            r[i]+=1

ans=((k*(1+k)*sum(r)//2) + (k*(k-1)*sum(l)//2))%MOD
print(ans)

