n=int(input())

if(n%2 == 1):
    print(0)
else:
    mod=10
    ans=0
    while(n >= mod):
        ans+=n//mod
        mod*=5
    print(ans)

# x=2 if n%2==0 else 3
# ans=1
# while(x <= n):
#     ans*=x
#     ansi=ans
#     modi=0
#     while(ansi%10 == 0):
#         modi+=1
#         ansi//=10
#     print(x,modi,((x//10)  + (x//50) + (x//250)))
#     x+=2

