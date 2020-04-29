h,w=map(int,input().split())
a=[]
used=[[False for _ in range(w)] for _ in range(h)]
ans=[]
for i in range(h):
    ai=list(map(int,input().split()))
    for j in range(w):
        if(ai[j]%2!=0):
            if(j<w-1 and ai[j]>0 and ai[j]%2!=0 and not used[i][j]):
                used[i][j]=True
                ai[j]-=1
                ai[j+1]+=1
                ans.append([i+1,j+1,i+1,j+2])
    a.append(ai)

for i in range(h):
    if(i<h-1 and a[i][w-1]>0 and a[i][w-1]%2!=0 and not used[i][w-1]):
        used[i][w-1]=True
        a[i][w-1]-=1
        a[i+1][w-1]+=1
        ans.append([i+1,w,i+2,w])

print(len(ans))
for i in range(len(ans)):
    print(*ans[i])
