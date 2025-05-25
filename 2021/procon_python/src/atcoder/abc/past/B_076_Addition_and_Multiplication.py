n=int(input())
k=int(input())

b=2**n
ans=999999999999999999
for i in range(b):
    bit_b=bin(i)[2:].zfill(n)
    ans_i=1
    for j in range(len(bit_b)):
        if(bit_b[j]=='0'):
            ans_i*=2
        elif(bit_b[j]=='1'):
            ans_i+=k

    if(ans>ans_i):
        ans=ans_i

print(ans)