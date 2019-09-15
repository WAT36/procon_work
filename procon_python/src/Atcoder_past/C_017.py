n,m=map(int,input().split())
linesum=[0 for i in range(m+1)]
sum_s=0
for i in range(n):
    li,ri,si=map(int,input().split())
    linesum[li-1] = linesum[li-1] + si
    linesum[ri] = linesum[ri] - si
    sum_s+=si
t=0
for i in range(m):
    t += linesum[i]
    linesum[i] = t
linesum.pop(-1)
print(sum_s-min(linesum))