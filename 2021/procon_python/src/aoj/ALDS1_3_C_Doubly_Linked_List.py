from collections import deque

n=int(input())
l=deque()
for i in range(n):
    com=input()
    if(com=="deleteFirst"):
        l.popleft()
    elif(com=="deleteLast"):
        l.pop()
    else:
        com,val=com.split()
        if(com=="insert"):
            l.appendleft(val)
        elif(com=="delete"):
            try:
                l.remove(val)
            except:
                pass

print(' '.join(l))
