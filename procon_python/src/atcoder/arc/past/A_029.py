n=int(input())
t=[]
for i in range(n):
    t.append(int(input()))

x=2**n
ans=999999999999
for i in range(x):
    binx=format(i, 'b').zfill(n)
    a=0
    b=0
    for j in range(n):
        if(binx[j] == "0"):
            a+=t[j]
        else:
            b+=t[j]
    if(ans > max(a,b)):
        ans = max(a,b)
print(ans)