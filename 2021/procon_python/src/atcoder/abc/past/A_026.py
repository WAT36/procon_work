a=int(input())
ans=0
for i in range(a//2 + 2):
    if(ans < i * (a-i)):
        ans =i * (a-i)
print(ans)
