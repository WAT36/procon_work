n=int(input())
d={}
for i in range(n):
    inst,val=input().split()
    if(inst=="insert"):
        d[val]=True
    elif(inst=="find"):
        if(d.get(val, False)):
            print("yes")
        else:
            print("no")