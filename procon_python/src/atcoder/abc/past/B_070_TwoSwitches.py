a,b,c,d=map(int,input().split())
ans=min(b,d)-max(a,c)
print(ans if ans>0 else 0)