n,h=map(int,input().split())
sword=[]
for i in range(n):
    a,b=map(int,input().split())
    sword.append([a,"a"])
    sword.append([b,"b"])
sword.sort()
ans=0
swordi=[0,"b"]
while(h>0):
    if(swordi[1]=="b"):
        swordi=sword.pop()
        ans+=1
        h-=swordi[0]
    else:
        attack=swordi[0]
        ans+= -(-h//attack)
        h-=attack * -(-h//attack)
print(ans)
