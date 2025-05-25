n=int(input())
d=list(map(int,input().split()))
sum_d=sum(d)
square_di=0
for i in range(n):
    square_di+=d[i]*d[i]
print((sum_d*sum_d - square_di)//2)