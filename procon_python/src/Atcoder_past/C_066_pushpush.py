n = int(input())
a = list(map(int,input().split()))
odd = a[0::2]
even = a[1::2]
ans = []
if n%2 == 0:
    even = even[::-1]
    ans = even + odd
else:
    odd = odd[::-1]
    ans = odd + even
for i in range(len(ans)):
    print(str(ans[i])+" ",end="")
print()