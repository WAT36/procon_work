import math
n=int(input())
point=[]
for i in range(n):
    point.append(list(map(int,input().split())))
ans=0
for i in range(n-1):
    for j in range(i+1,n):
        dist= math.sqrt((point[j][0] - point[i][0])**2 + (point[j][1] - point[i][1])**2)
        if(ans < dist):
            ans = dist
print(ans)