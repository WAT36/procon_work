import collections
MOD=1000000007
n=int(input())
t=[]
for i in range(n):
    t.append(int(input()))

t.sort()
ans_pena=0
accum=0
for i in range(n):
    accum+=t[i]
    ans_pena+=accum


ans_pattern=1
t_pattern=collections.Counter(t)
fact=[1 for _ in range(max(t_pattern.values())+1)]
for i in range(1,len(fact)):
    fact[i]=fact[i-1]*i

for k,v in t_pattern.items():
    ans_pattern=((ans_pattern%MOD)*(fact[v]%MOD))%MOD

print(ans_pena)
print(ans_pattern)