s=input()
ans=0
up=0
down=0
if(s[0]=='>'):
    down+=1
else:
    up+=1


for i in range(1,len(s)):
    if(s[i]=='>'):
        down+=1
    else:
        if(s[i-1]=='>'):
            high=max(up,down)
            low=min(up,down)
            ans+=(high+1)*(0+high)//2
            low-=1
            ans+=(low+1)*(0+low)//2
            up=1
            down=0
        else:
            up+=1
else:
    high=max(up,down)
    low=min(up,down)
    ans+=(high+1)*(0+high)//2
    low-=1
    ans+=(low+1)*(0+low)//2
print(ans)