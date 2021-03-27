n=int(input())
a=list(map(int,input().split()))

ans=float('inf')

for i in range(2**(n-1)):

#    sikiri=bin(i)[2:].zfill(n-1)

    ansi=0
    ori=0
    for j in range(n):
        ori|=a[j]
#        if(j==n-1 or sikiri[j]=='1'):
        if(i>>j&1):
            ansi^=ori
            ori=0
    ansi^=ori
    ans=min(ans,ansi)

print(ans)
