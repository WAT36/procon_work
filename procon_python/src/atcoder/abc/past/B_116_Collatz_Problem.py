s=int(input())
a=[]
ai=s
i=1
while(ai not in a):
    a.append(ai)
    i+=1
    if(ai%2==0):
        ai//=2
    else:
        ai = 3*ai + 1
print(i)
