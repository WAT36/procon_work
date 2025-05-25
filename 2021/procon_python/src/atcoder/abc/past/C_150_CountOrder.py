import math
n=int(input())
p=list(map(int,input().split()))
q=list(map(int,input().split()))

pjun=[i+1 for i in range(n)]
qjun=[i+1 for i in range(n)]

pord=0
qord=0
for i in range(n):
    pi=p[i]
    pord+=pjun.index(pi)*math.factorial(len(pjun)-1)
    pjun.remove(pi)

    qi=q[i]
    qord+=qjun.index(qi)*math.factorial(len(qjun)-1)
    qjun.remove(qi)

print(abs(pord-qord))
