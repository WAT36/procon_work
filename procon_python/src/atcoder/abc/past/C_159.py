l=int(input())
ans=0

y=l
z=(l-y)/2
x=l-y-z
ans=max(ans,x*y*z)

y=l/3
z=(l-y)/2
x=l-y-z
ans=max(ans,x*y*z)


print(ans)