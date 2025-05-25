import bisect
n,m,x=map(int,input().split())
a=list(map(int,input().split()))
left=bisect.bisect(a,x)
right=len(a)-left
print(min(left,right))