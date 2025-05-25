a=[]
for i in range(3):
    a.extend(list(map(int,input().split())))

n=int(input())
for i in range(n):
    b=int(input())
    if(b in a):
        a[a.index(b)] = -1

if((a[0]==-1 and a[3]==-1 and a[6]==-1) or
   (a[1]==-1 and a[4]==-1 and a[7]==-1) or
   (a[2]==-1 and a[5]==-1 and a[8]==-1) or
   (a[0]==-1 and a[1]==-1 and a[2]==-1) or
   (a[3]==-1 and a[4]==-1 and a[5]==-1) or
   (a[6]==-1 and a[7]==-1 and a[8]==-1) or
   (a[0]==-1 and a[4]==-1 and a[8]==-1) or
   (a[2]==-1 and a[4]==-1 and a[6]==-1)):
    print("Yes")
else:
    print("No")
