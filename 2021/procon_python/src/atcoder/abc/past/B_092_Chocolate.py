n=int(input())
d,x=map(int,input().split())
choco=x
for i in range(n):
    a=int(input())
    day=1
    while(day<=d):
        choco+=1
        day+=a
print(choco)