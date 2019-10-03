n=int(input())
n30=n%30
mostleft=(-(-n30//5)+1) if (-(-n30//5)+1) <= 6 else 1
ind=n30%5 if n30%5!=0 else 5
ans=[]
num=mostleft
for i in range(6):
    if(i==ind):
        ans.append(str(mostleft-1 if mostleft!=1 else 6))
    else:
        ans.append(str(num))
        num+=1
        if(num>=7):
            num=1
print("".join(ans))