abc=list(map(int,input().split()))
k=int(input())
abc.sort()
print(abc[0]+abc[1]+(abc[2]*(2**k)))
