import math
n=int(input())
loc=[]
for i in range(n):
    loc.append(list(map(int,input().split())))

d_sum=0
for i in range(n-1):
    for j in range(i+1,n):
        x=(loc[j][0]-loc[i][0])**2
        y=(loc[j][1]-loc[i][1])**2
        dij=math.sqrt(x + y)
        d_sum+=dij
print(2*d_sum/n)