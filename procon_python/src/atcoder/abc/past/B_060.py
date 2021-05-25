a,b,c=map(int,input().split())

amari=set([])
i=1
while(True):
    amari_i=(i*a)%b
    if(amari_i in amari):
        break
    else:
        amari.add(amari_i)
    i+=1

if(c in amari):
    print('YES')
else:
    print('NO')
