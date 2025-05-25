n=input()
sn=0
for i in range(len(n)):
    sn+=int(n[i])
n=int(n)
if(n%sn==0):
    print("Yes")
else:
    print("No")
