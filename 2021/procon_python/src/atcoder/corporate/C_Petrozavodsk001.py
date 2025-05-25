import sys
n=int(input())

print(0)
sexlow=input()
if(sexlow=='Vacant'):
    sys.exit()

print(n-1)
sexhigh=input()
if(sexhigh=='Vacant'):
    sys.exit()

low=0
high=n-1
piv=0
while(True):
    piv=(low+high)//2

    print(piv)
    sexn=input()
    if(sexn=='Vacant'):
        break
    elif(( (piv-low)%2==0 and sexlow!=sexn) or ( (piv-low)%2!=0 and sexlow==sexn)):
        high=piv
        sexhigh=sexn
    elif(( (high-piv)%2==0 and sexhigh!=sexn) or ( (high-piv)%2!=0 and sexhigh==sexn)):
        low=piv
        sexlow=sexn

