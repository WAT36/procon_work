import sys
a=[]
for i in range(4):
    a.append(list(map(int,input().split())))

for i in range(4):
    for j in range(4):
        if(i<3 and j<3 and (a[i][j]==a[i+1][j] or a[i][j]==a[i][j+1])):
            print("CONTINUE")
            sys.exit()
        elif(i==3 and j==3):
            pass
        elif(i==3 and (a[i][j]==a[i][j+1])):
            print("CONTINUE")
            sys.exit()
        elif(j==3 and (a[i][j]==a[i+1][j])):
            print("CONTINUE")
            sys.exit()

print("GAMEOVER")
