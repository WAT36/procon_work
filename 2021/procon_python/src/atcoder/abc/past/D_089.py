h,w,d=map(int,input().split())
a=[]
box=[[] for i in range(h*w+1)]
wi=0
for i in range(h):
    ai=list(map(int,input().split()))
    for j in range(w):
        box[ai[j]]=[i,j]

p=[0]
for i in range(1,h*w+1):
    if(i-d>0):
        p.append(p[i-d]+abs(box[i][0]-box[i-d][0])+abs(box[i][1]-box[i-d][1]))
    else:
        p.append(0)

q=int(input())
for i in range(q):
    l,r=map(int,input().split())
    print(p[r]-p[l])
