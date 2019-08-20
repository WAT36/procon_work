S = str(input())
l = list(map(str,(map(bin,range(2**(len(S)-1))))))

ans = 0
for i in range(len(l)):
    ev = l[i][2:].zfill(len(S)-1)
    res = 0
    num_str = S[0]
    for j in range(1,len(S)):
        if(ev[j-1] == '0'):
            num_str = num_str + S[j]
        else:
            res += int(num_str)
            num_str = S[j]
    res += int(num_str)
    ans += res

print(ans)