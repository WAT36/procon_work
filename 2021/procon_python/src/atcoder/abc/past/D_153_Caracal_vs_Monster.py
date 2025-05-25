from collections import deque
h=int(input())
q=deque()
count=0
q.append(h)
while(len(q)>0):
    hi=q.popleft()
    if(hi==1):
        pass
    else:
        attacked_hi=hi//2
        q.append(attacked_hi)
    count+=1

ans=0
for i in range(count):
    ans+=(2**i)
print(ans)
