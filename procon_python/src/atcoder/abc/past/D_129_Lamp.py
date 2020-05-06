import numpy as np
h,w=map(int,input().split())
s=[]
for _ in range(h):
    si=input()
    si=si.replace('.', '1')
    si=si.replace('#', '0')
    s.append(list(map(int,si)))
s=np.array(s)

left=np.zeros((h,w))
right=np.zeros((h,w))
up=np.zeros((h,w))
down=np.zeros((h,w))

for i in range(w):
    if(i==0):
        left[:,i]=s[:,i]
        right[:,w-i-1]=s[:,w-i-1]
    else:
        left[:,i]=(left[:,i-1]+1)*s[:,i]
        right[:,w-i-1]=(right[:,w-i]+1)*s[:,w-i-1]

for i in range(h):
    if(i==0):
        down[i,:]=s[i,:]
        up[h-i-1,:]=s[h-i-1,:]
    else:
        down[i,:]=(down[i-1,:]+1)*s[i,:]
        up[h-i-1,:]=(up[h-i,:]+1)*s[h-i-1,:]

ans=left+right+up+down-3
print(int(np.max(ans)))
