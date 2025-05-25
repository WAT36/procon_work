n,k,q=map(int,input().split())
a=[int(input()) for x in range(q)]
point=[k-q for x in range(n)]
for i in range(q):
    point[a[i]-1]+=1

for i in range(n):
    if(point[i] > 0):
        print("Yes")
    else:
        print("No")