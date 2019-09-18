import sys
n,k=map(int,input().split())
t=[]
for i in range(n):
    ti = list(map(int,input().split()))
    t.append(ti)

for i in range(n**k):
    temp = i
    res = 0
    for j in range(n):
        res = res ^ t[j][temp%k]
        temp //= k
    if(res == 0):
        print("Found")
        sys.exit()
print("Nothing")