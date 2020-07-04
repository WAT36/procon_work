import math
l=sorted(list(map(int,input().split())))

loabc_long=sum(l)
loabc_short=0
if(l[0]+l[1]<l[2]):
    loabc_short=l[2]-(l[1]+l[0])

print( ( math.pi * (loabc_long**2) ) -
       ( math.pi * (loabc_short**2) ) )

