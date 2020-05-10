n,k=map(int,input().split())
a=list(map(int,input().split()))
roop=[]
roop_set=set([])

a.insert(0, 0)
s=1
for i in range(k):
    s=a[s]
    if(s not in roop_set):
        roop.append(s)
        roop_set.add(s)
    else:
        s_first=roop.index(s)
        roop=roop[s_first:]
        k-=(s_first+1)
#        print(k,roop,s_first)
        print(roop[k%len(roop)])
        break
else:
#    print(roop,k)
    print(roop[k-1])