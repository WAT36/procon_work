n,m=map(int,input().split())
box=[False for _ in range(n)]
box[0]=True
ball=[1 for _ in range(n)]
for i in range(m):
    x,y=map(int,input().split())
    ball[x-1]-=1
    ball[y-1]+=1
    if(box[x-1]==True):
        box[y-1]=True
    if(ball[x-1]<=0):
        box[x-1]=False
print(box.count(True))
#print(box)
#print(ball)