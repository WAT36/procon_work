n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
sum_vote=sum(a)
least_vote=sum_vote/(4*m)
if(a[-1*m]>=least_vote):
    print("Yes")
else:
    print("No")