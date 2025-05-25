from collections import deque
n=int(input())

alpha=list('abcdefghijk')

q=deque([])
q.append(alpha[0])

for i in range(1,n):
    qi=deque([])

    while(len(q)>0):
        qij=q.popleft()
        qij_setnum=len(set(list(qij)))
        for j in range(qij_setnum+1):
            qi.append(qij+alpha[j])

    q=qi

q=list(q)
q.sort()
for i in range(len(q)):
    print(q[i])