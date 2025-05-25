import math
n=int(input())
root_n=int(math.sqrt(n)//1)
ans=9999999999999
for i in range(1,root_n+1):
    tate=i
    yoko=n//i
    rest=n-(tate*yoko)
    ans = min(ans,abs(tate-yoko)+rest)
print(ans)