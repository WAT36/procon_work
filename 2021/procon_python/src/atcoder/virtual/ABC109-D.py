h,w=map(int,input().split())
a=[]
for i in range(h):
    a.append(list(map(int,input().split())))

ans=[]
for i in range(h):
    for j in range(w):
        if(j==w-1 and i!=h-1 and a[i][j]%2!=0):
            a[i][j]-=1
            a[i+1][j]+=1
            ans.append([i+1,j+1,i+2,j+1])
        elif(j<w-1 and a[i][j]%2!=0):
            a[i][j]-=1
            a[i][j+1]+=1
            ans.append([i+1,j+1,i+1,j+2])

print(len(ans))
for i in range(len(ans)):
    print(*ans[i])
