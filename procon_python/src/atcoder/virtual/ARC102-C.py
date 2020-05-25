n,k=map(int,input().split())

ans=0
for b in range(1,n+1):
    if((n+b)//k >0 and (2*b)%k==0):
        p=((n+b)//k)
        q=(-(-b//k)) if b%k!=0 else (b//k)+1
        ans+=( p - q + 1)**2

#         for i in range( q,p+1):
#             for j in range( q,p+1):
#                 print(i*k-b,b,j*k-b)

print(ans)