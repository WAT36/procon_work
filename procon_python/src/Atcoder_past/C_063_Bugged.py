N = int(input())

s = []
sum = 0
min_nonten = 999
all_ten = True
for i in range(N):
    s.append(int(input()))
    sum += s[i]
    if(s[i] % 10 != 0):
        all_ten = False
        if(min_nonten > s[i]):
            min_nonten = s[i]


if(sum % 10 != 0):
    print(sum)
elif(all_ten):
    print(0)
else:
    print(sum - min_nonten)