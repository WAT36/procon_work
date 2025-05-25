import sys
n=int(input())
d=list(map(int,input().split()))

if(d[0]!=0 or d.count(0)>1):
    print(0)
    sys.exit()

MOD=998244353
max_d=max(d)
c=[0 for _ in range(max_d+1)]
for i in range(n):
    c[d[i]]+=1

ans=1
for i in range(max_d):
    ans*=c[i] ** c[i+1]
print(ans%MOD)
