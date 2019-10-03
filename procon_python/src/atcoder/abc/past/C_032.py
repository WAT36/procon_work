import sys
n,k=map(int,input().split())
s=[]
flag=False
for i in range(n):
    s.append(int(input()))
    if(s[i] == 0):
        flag = True

if(flag):
    print(n)
    sys.exit()
start=0
end=0
v=s[0]
ans=0
while(True):
    if(v <= k):
        if(ans < end - start + 1):
            ans = end - start + 1
        end += 1
        if(end >= n):
            break
        v *= s[end]
    else:
        if(start >= n):
            break
        v /= s[start]
        start += 1
        if(start < n and end < start):
            end = start
            v = s[start]
print(ans)