n=int(input())

ans=9999999999999
for a in range(1,n):
    b=n-a
    a_sum=sum(list(map(int,list(str(a)))))
    b_sum=sum(list(map(int,list(str(b)))))
    ab_sum=a_sum+b_sum
    if(ans>ab_sum):
        ans=ab_sum
#        print(a,b,ab_sum)
print(ans)
