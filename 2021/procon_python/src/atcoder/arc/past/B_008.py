n,m=map(int,input().split())
name=input()
kit=input()
name_w={}
kit_w={}

for i in range(n):
    ni=name_w.get(name[i], 0)
    name_w[name[i]]=ni+1

for i in range(m):
    ki=kit_w.get(kit[i], 0)
    kit_w[kit[i]]=ki+1

max_short=0
for k,v in name_w.items():
    kit_ni=kit_w.get(k, -1)
#    print(k,v,kit_ni)
    if(kit_ni==-1):
        print(-1)
        break
    else:
        short_num=-(-v//kit_ni)
        if(max_short<short_num):
            max_short=short_num
else:
    print(max_short)
