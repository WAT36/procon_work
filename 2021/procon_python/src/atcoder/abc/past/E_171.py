n=int(input())
a=list(map(int,input().split()))

a_xor_sum=0
for ai in a:
    a_xor_sum = a_xor_sum ^ ai

ans=[]
for ai in a:
    ans.append(a_xor_sum ^ ai)

print(*ans)