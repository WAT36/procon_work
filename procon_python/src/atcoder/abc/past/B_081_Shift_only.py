n=int(input())
a=list(map(int,input().split()))
ans=99999999999999999
for ai in a:
    c=0
    while(ai%2==0):
        ai//=2
        c+=1

    if(ans>c):
        ans=c
print(ans)
