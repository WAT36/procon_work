n,m=map(int,input().split())
b=[]
for i in range(n):
    b.append(list(map(int,list(input()))))

a=[[0 for _ in range(m)] for _ in range(n)]

def edge_search(lx,ly,rx,ry):

    for y in range(ly,ry+1):
        if(y==ly or y==ry):
            for x in range(lx,rx+1):
                if(b[y][x]==0):
                    continue
                elif(y==ly):
                    a[y+1][x]+=b[y][x]
                    if(x>lx):
                        b[y+1][x-1]-=b[y][x]
                    if(x<rx):
                        b[y+1][x+1]-=b[y][x]
                    b[y+2][x]-=b[y][x]
                    b[y][x]-=b[y][x]
                else:
                    a[y-1][x]+=b[y][x]
                    if(x>lx):
                        b[y-1][x-1]-=b[y][x]
                    if(x<rx):
                        b[y-1][x+1]-=b[y][x]
                    b[y-2][x]-=b[y][x]
                    b[y][x]-=b[y][x]

        else:
            if(b[y][lx]==0):
                pass
            else:
                a[y][lx+1]+=b[y][lx]
                b[y-1][lx+1]-=b[y][lx]
                b[y+1][lx+1]-=b[y][lx]
                b[y][lx+2]-=b[y][lx]
                b[y][lx]-=b[y][lx]

            if(b[y][rx]==0):
                pass
            else:
                a[y][rx-1]+=b[y][rx]
                b[y-1][rx-1]-=b[y][rx]
                b[y+1][rx-1]-=b[y][rx]
                b[y][rx-2]-=b[y][rx]
                b[y][rx]-=b[y][rx]


#     print("----a")
#     for i in range(len(a)):
#         print(''.join([str(a[i][j]) for j in range(len(a[i]))]))
# 
#     print("----b")
#     for i in range(len(b)):
#         print(''.join([str(b[i][j]) for j in range(len(b[i]))]))


lx=0
ly=0
rx=m-1
ry=n-1
while(lx<rx and ly<ry):
    edge_search(lx, ly, rx, ry)
    lx+=1
    ly+=1
    rx-=1
    ry-=1

for i in range(len(a)):
    print(''.join([str(a[i][j]) for j in range(len(a[i]))]))
