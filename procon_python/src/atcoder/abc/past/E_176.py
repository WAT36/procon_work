h,w,m=map(int,input().split())
coops=[]
hlists=[0 for _ in range(h+1)]
wlists=[0 for _ in range(w+1)]
for i in range(m):
    hi,wi=map(int,input().split())
    hlists[hi]+=1
    wlists[wi]+=1
    coops.append([hi,wi])

max_h=max(hlists)
max_hlists=set([i for i, x in enumerate(hlists) if x == max_h])
max_w=max(wlists)
max_wlists=set([i for i, x in enumerate(wlists) if x == max_w])

kyotu=0
for i in range(len(coops)):
    if(coops[i][0] in max_hlists and coops[i][1] in max_wlists):
        kyotu+=1


if(kyotu==len(max_hlists)*len(max_wlists)):
    print(max_h+max_w-1)
else:
    print(max_h+max_w)
