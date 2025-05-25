n,m,a,b=map(int,input().split())
cards=n
for i in range(m):
    if(cards<=a):
        cards+=b

    c=int(input())
    cards-=c

    if(cards<0):
        print(i+1)
        cards+=b
        break
else:
    print('complete')