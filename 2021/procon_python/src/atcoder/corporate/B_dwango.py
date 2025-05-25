import math
s=input()
ans=0
ind=s.find('25',0)
pre_ind=ind-2
nico=0

while(ind != -1):
    if(ind-pre_ind==2):
        nico+=1
    else:
        ans+=nico*(1+nico)//2
        nico=1
    pre_ind=ind
    ind=s.find('25',ind+1)
#    print(ans,pre_ind,ind)
else:
    ans+=nico*(1+nico)//2

print(ans)

