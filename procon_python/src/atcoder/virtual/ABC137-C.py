n=int(input())
d={}
for i in range(n):
    si=''.join(list(sorted(input())))
    d[si]=d.get(si, 0)+1

ans=0
for v in d.values():
    if(v>1):
        ans+=v*(v-1)//2
print(ans)