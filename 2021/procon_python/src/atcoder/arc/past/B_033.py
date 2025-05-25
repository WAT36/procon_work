na,nb=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

ans=len(set(a)&set(b))/len(set(a)|set(b))
print(ans)

