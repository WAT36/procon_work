import sys
n,m,k=map(int,input().split())


for p in range(n+1):
    for q in range(m+1):
        ans=p*m + q*n - 2*p*q
        if(ans==k):
            print('Yes')
            sys.exit()
else:
    print('No')
