n,a,b=map(int,input().split())
ans=0
for i in range(n+1):
    sumi=0
    stri=list(str(i))
    for stri_i in stri:
        sumi+=int(stri_i)

    if(a<=sumi and sumi<=b):
        ans+=i
print(ans)