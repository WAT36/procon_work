n,k=map(int,input().split())

if(n==k):
    print(0)
elif(n>k):
    n=n-k*(n//k)
    print(min(n,abs(n-k)))
else:
    print(min(n,abs(n-k)))