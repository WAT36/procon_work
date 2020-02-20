n=int(input())
a=list(map(int,input().split()))
a=[ai for ai in a if ai>0]
print(-(-sum(a)//len(a)))
