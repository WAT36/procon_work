x=int(input())
i=0
ans=0
while(True):
    i+=x
    ans+=1
    if(i%360==0):
        print(ans)
        break