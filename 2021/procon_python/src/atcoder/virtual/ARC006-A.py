e=list(input().split())
b=list(input())
l=list(input().split())

coincide=0
bonus=0
for i in range(6):
    if(l[i] in e):
        coincide+=1

    if(l[i]==b[0]):
        bonus+=1

if(coincide==6):
    print(1)
elif(coincide==5 and bonus>0):
    print(2)
elif(coincide==5 and bonus==0):
    print(3)
elif(coincide==4):
    print(4)
elif(coincide==3):
    print(5)
else:
    print(0)