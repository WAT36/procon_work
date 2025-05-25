n=int(input())
vote={}
for i in range(n):
    si=input()
    vi=vote.get(si, 0)
    vote[si]=vi+1

max_v=max(vote.values())

ans=[]
for k,v in vote.items():
    if(v==max_v):
        ans.append(k)
ans.sort()
for i in range(len(ans)):
    print(ans[i])