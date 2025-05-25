N = int(input())
s = []
for i in range(N):
    si = list(input())
    s.append(''.join(sorted(si)))

s.sort()

ans = 0
pre_same = 1
for i in range(1,N):
#    print("a,s[i]:" + s[i]+",pre_same:" + str(pre_same) + ",ans:" + str(ans))
    if(s[i-1] == s[i]):
        pre_same = pre_same +1
    else:
        if(pre_same > 1):
            ans = ans + (pre_same * (pre_same-1) / 2)
        pre_same = 1
#    print("b,s[i]:" + s[i]+",pre_same:" + str(pre_same) + ",ans:" + str(ans))

if(pre_same > 1):
    ans = ans + (pre_same * (pre_same-1) / 2)

print(int(ans))