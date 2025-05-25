n=int(input())
s=list(map(int,input().split()))
q=int(input())
t=list(map(int,input().split()))

ans=list(set(s) & set(t))
print(len(ans))
