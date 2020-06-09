n=int(input())
d={}
dlist=list(map(int,input().split()))
for i in range(len(dlist)):
    d[dlist[i]]=d.get(dlist[i], 0)+1


m=int(input())
t={}
tlist=list(map(int,input().split()))
for i in range(len(tlist)):
    t[tlist[i]]=t.get(tlist[i], 0)+1


for tk,tv in t.items():
    if(d.get(tk, 0)<tv):
        print("NO")
        break
else:
    print("YES")

