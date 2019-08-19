x = int(input())

ans = x // 11

if(ans * 11 == x):
    print(ans*2)
elif((ans * 11)+6 >= x):
    print(ans*2 + 1)
else:
    print(ans*2 + 2)
