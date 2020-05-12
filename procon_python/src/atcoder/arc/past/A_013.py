n,m,l=sorted(list(map(int,input().split())))
p,q,r=sorted(list(map(int,input().split())))

ans=0
ans=max(ans,(n//p)*(m//q)*(l//r))
ans=max(ans,(n//p)*(m//r)*(l//q))
ans=max(ans,(n//q)*(m//p)*(l//r))
ans=max(ans,(n//q)*(m//r)*(l//p))
ans=max(ans,(n//r)*(m//p)*(l//q))
ans=max(ans,(n//r)*(m//q)*(l//p))
print(ans)