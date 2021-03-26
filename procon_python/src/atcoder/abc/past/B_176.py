n=input()
sumn=0
for i in range(len(n)):
    sumn+=int(n[i])

if(sumn%9==0):
    print('Yes')
else:
    print('No')