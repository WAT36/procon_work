import math
n=int(input())
a=list(map(int,input().split()))

sum_a=sum(a)
left_a=0
right_a=sum_a
ans=200002*2020202020

for i in range(n):
    left_a+=a[i]
    right_a-=a[i]
    if(ans>abs(left_a-right_a)):
        ans=abs(left_a-right_a)
print(ans)