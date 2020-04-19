import sys
n,k=map(int,input().split())
s=input()
snum=[]
now_si=""
now_sinum=0
for i in range(len(s)):
    if(now_si!=s[i]):
        now_si=s[i]
        snum.append(now_sinum)
        now_sinum=1
    else:
        now_sinum+=1
else:
    snum.append(now_sinum)
snum.pop(0)

if(len(snum)<3):
    print(sum(snum)-1)
    sys.exit()

for i in range(k):
#    print(snum)
    if(len(snum)<3):
        snum=[sum(snum)]
        break

    snum[-3]+=snum[-2]+snum[-1]
    snum.pop(-1)
    snum.pop(-1)

print(sum(snum)-len(snum))