r,c,d=map(int,input().split())
a=[]
for i in range(r):
    a.append(list(map(int,input().split())))

ans=[]
if(d%2==0):
    for i in range(r):
        for j in range(c):
            if((i+j)%2!=0):
                continue
            elif(i+j>d):
                break
            else:
                ans.append(a[i][j])
else:
    for i in range(r):
        for j in range(c):
            if((i+j)%2==0):
                continue
            elif(i+j>d):
                break
            else:
                ans.append(a[i][j])
print(max(ans))