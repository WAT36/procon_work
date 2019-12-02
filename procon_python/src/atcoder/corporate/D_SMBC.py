n=int(input())
s=input()
ans=0
for i in range(10):
    for j in range(10):
        for k in range(10):
            x=s.find(str(i))
            y=s.find(str(j),x+1)
            z=s.find(str(k),y+1)
            if(x!=-1 and y!=-1 and z!=-1):
                ans+=1
print(ans)