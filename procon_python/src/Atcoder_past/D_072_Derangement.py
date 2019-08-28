N=int(input())
p=list(map(int,input().split()))
count=0
series=0
for i in range(N):
    if(p[i]-1 == i):
        series += 1
    elif(series > 0):
        count += -(-series//2)
        series=0
if(series > 0):
    count += -(-series//2)
print(count)