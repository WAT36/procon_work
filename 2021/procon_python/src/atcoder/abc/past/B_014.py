n,x=map(int,input().split())
a=list(map(int,input().split()))

bin_x=''.join(reversed(list(bin(x)[2:].zfill(n))))
ans=0
for i in range(n):
    if(bin_x[i]=="1"):
        ans+=a[i]
print(ans)
