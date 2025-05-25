a,b,k=map(int,input().split())
ans=[i for i in range(a,min(b,a+k))]
ans.extend([i for i in range(max(a,b-k+1),b+1)])
ans=sorted(list(set(ans)))
for ansi in ans:
    print(ansi)