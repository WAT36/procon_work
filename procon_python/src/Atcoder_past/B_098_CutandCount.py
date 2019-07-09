N = int(input())
S = input()

pre={}
back={}

for i in range(len(S)):
    n = pre.get(S[i], 0)
    n = n+1
    pre[S[i]] = n

ans = 0
for i in range(len(S)):
    n = pre[S[i]]
    if(n > 1):
        pre[S[i]] = n-1
    else:
        pre.pop(S[i])
    back[S[i]] = back.get(S[i], 0) + 1
    c = [x for x in list(pre.keys()) if x in list(back.keys())]
    ans = max(ans,len(c))

print(ans)