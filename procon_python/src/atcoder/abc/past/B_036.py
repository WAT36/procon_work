n=int(input())
s=[]
for i in range(n):
    s.append(list(input()))

for i in range(n):
    si=[]
    for j in range(n-1,-1,-1):
        si.append(s[j][i])
    print(''.join(si))
