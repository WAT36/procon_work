n,l=map(int,input().split())
s=[]

for i in range(l+1):
    s.append(input())


x=s[l].index('o')
y=l-1
while(y>=0):
    if(x>0 and s[y][x-1]=='-'):
        x-=2
    elif(x<len(s[y])-1 and s[y][x+1]=='-'):
        x+=2

    y-=1
print(x//2 + 1)
