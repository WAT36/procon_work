import sys
n=int(input())
a=list(map(int,input().split()))
sum_a=sum(a)

if(sum_a%n!=0):
    print(-1)
    sys.exit()

personnum=sum_a//n
ans=0

person_i=0
islands_num=0
for i in range(n):
    person_i+=a[i]
    islands_num+=1
    if(person_i%islands_num==0 and person_i//islands_num==personnum):
        person_i=0
        islands_num=0
    else:
        ans+=1
print(ans)
