from collections import Counter
n,m=map(int,input().split())
name=Counter(list(input()))
kit=Counter(list(input()))

#print(name)
#print(kit)

ans=0
for k,v in name.items():
    kit_v=kit.get(k, 0)
    if(kit_v==0):
        ans=-1
        break
    else:
        ans=max(ans,-(-v//kit_v))

print(ans)