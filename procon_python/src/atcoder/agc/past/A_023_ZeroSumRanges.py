n=int(input())
a=list(map(int,input().split()))

#累積和
ans=0
acum={}
acumi=0
for i in range(n):
    acumi+=a[i]
    acum[acumi]=acum.get(acumi, 0)+1

for k,v in acum.items():
    if(k==0):
        ans+=v*(1+v)//2
    else:
        ans+=(v-1)*v//2
print(ans)
