import sys
def routeSearch(x,y):
    a[y][x]='@'
    if(x<w-1 and a[y][x+1]=='#'):
        routeSearch(x+1,y)
    elif(y<h-1 and a[y+1][x]=='#'):
        routeSearch(x,y+1)
h,w=map(int,input().split())

a=[]
for i in range(h):
    a.append(list(input()))

routeSearch(0,0)
for i in range(h):
    if('#' in a[i]):
        print("Impossible")
        sys.exit()

print("Possible")
