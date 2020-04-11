n=int(input())
ans=0
for i in range(n):
    a,b,c,d,e=map(int,input().split())
    score=a+b+c+d+(e*110/900)
    if(ans<score):
        ans=score
print(ans)