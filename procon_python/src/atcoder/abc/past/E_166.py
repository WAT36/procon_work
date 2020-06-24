import collections

def list_count(l):
    return collections.Counter(l)

n=int(input())
a=list(map(int,input().split()))

l=[i+a[i] for i in range(len(a))]
m=[i-a[i] for i in range(len(a))]

mlist=list_count(m)

mlist0=mlist[m[0]]
mlist[m[0]]=mlist0-1

ans=0
for i in range(len(l)-1):
    ansi=mlist.get(l[i], 0)
    ans+=ansi

    mlist[m[i]]=mlist[m[i]]-1

print(ans)
