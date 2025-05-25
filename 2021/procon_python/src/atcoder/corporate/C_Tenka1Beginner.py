from collections import deque
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
a.sort()
a=deque(a)
ans=0

big=a.pop()
small=a.popleft()
ans+=big-small
#print(ans,a,big,small)
pre_big=big
pre_small=small
checked_a=deque([small,big])
while(len(a)>1):
    big=a.pop()
    small=a.popleft()
    ans+=pre_big-small
    ans+=big-pre_small
#    print(ans,a,big,small,pre_big,pre_small)
    pre_big=big
    pre_small=small

if(len(a)==1):
    last_a=a.pop()
    ans+=max(pre_big-last_a,last_a-pre_small)

print(ans)

