import copy

n = int(input())
a = list(map(int,input().split()))
sum = 0

ans_a = 0
for i in range(len(a)):
    sum += a[i]
    if(i%2 == 0):
        if(sum >= 0):
            ans_a += sum + 1
            sum = -1
    else:
        if(sum <= 0):
            ans_a += 1 - sum
            sum = 1

sum = 0
ans_b = 0
for i in range(len(a)):
    sum += a[i]
    if(i%2 == 0):
        if(sum <= 0):
            ans_b += 1 - sum
            sum = 1
    else:
        if(sum >= 0):
            ans_b += sum + 1
            sum = -1

print(min(ans_a,ans_b))