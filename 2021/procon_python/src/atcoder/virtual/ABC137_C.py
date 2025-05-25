n=int(input())
sd={}
for i in range(n):
    si=''.join(sorted(list(input())))
    sd[si]=sd.get(si, 0)+1

ans=0
for v in sd.values():
    if(v>1):
        ans+=((v*(v-1))//2)
print(ans)