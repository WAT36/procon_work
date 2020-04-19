from collections import deque
n=int(input())

alpha=['a','b','c','d','e','f','g','h','i','j','k']

q=deque(['a'])

for i in range(n-1):
    qi_ans=[]
    while(len(q)>0):
        qi=q.popleft()
        qiword_maxind=0
        for j in range(len(qi)):
            qi_ans.append(qi+qi[j])
            qij_ind=alpha.index(qi[j])
            if(qiword_maxind<qij_ind):
                qiword_maxind=qij_ind
        else:
            qi_ans.append(qi+alpha[qiword_maxind+1])
    qi_ans=sorted(list(set(qi_ans)))
#    print(qi_ans)
    q.extend(qi_ans)

lenq=len(q)
for i in range(lenq):
    print(q.popleft())
