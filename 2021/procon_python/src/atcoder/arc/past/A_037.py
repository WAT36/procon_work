n=int(input())
m=list(map(int,input().split()))
ans=0
for i in range(n):
    ans+= 80-m[i] if 80>m[i] else 0
print(ans)
