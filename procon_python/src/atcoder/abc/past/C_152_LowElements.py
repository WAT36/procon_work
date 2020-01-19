n=int(input())
p=list(map(int,input().split()))
ans=0
min_pj=p[0]
for pi in p:
    min_pj=min(min_pj,pi)
    if(min_pj>=pi):
        ans+=1
print(ans)
