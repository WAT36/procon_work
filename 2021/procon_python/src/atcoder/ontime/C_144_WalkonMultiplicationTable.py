import math
n=int(input())
ans=10**12
sqrt_n=math.ceil(math.sqrt(n))
for i in range(1,sqrt_n+1):
    if(n%i==0 and ans > i+(n//i)-2):
        ans = i + (n//i) - 2
print(ans)