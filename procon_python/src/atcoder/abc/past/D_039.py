import copy
h,w=map(int,input().split())
s=[]
scopy=[]
ans=[['.' for _ in range(w)] for _ in range(h)]

for i in range(h):
    s.append(list(input()))

scopy=copy.deepcopy(s)

def wasWhite(x,y):
    if(s[y][x]=='.'):
        return False
    else:
        if(x>0 and s[y][x-1]=='.'):
            return False
        if(x<w-1 and s[y][x+1]=='.'):
            return False
        if(y>0 and s[y-1][x]=='.'):
            return False
        if(y<h-1 and s[y+1][x]=='.'):
            return False
        if(x>0 and y>0 and s[y-1][x-1]=='.'):
            return False
        if(x>0 and y<h-1 and s[y+1][x-1]=='.'):
            return False
        if(x<w-1 and y>0 and s[y-1][x+1]=='.'):
            return False
        if(x<w-1 and y<h-1 and s[y+1][x+1]=='.'):
            return False
        return True

def whitePaint(x,y):
    scopy[y][x]='.'
    if(x>0):
        scopy[y][x-1]='.'
    if(x<w-1):
        scopy[y][x+1]='.'
    if(y>0):
        scopy[y-1][x]='.'
    if(y<h-1):
        scopy[y+1][x]='.'
    if(x>0 and y>0):
        scopy[y-1][x-1]='.'
    if(x>0 and y<h-1):
        scopy[y+1][x-1]='.'
    if(x<w-1 and y>0):
        scopy[y-1][x+1]='.'
    if(x<w-1 and y<h-1):
        scopy[y+1][x+1]='.'


for i in range(h):
    for j in range(w):
        if(wasWhite(j, i)):
            ans[i][j]='#'
            whitePaint(j, i)

# print(s)
# print(scopy)
# print(ans)

for i in range(h):
    if('#' in scopy[i]):
        print("impossible")
        break
else:
    print('possible')
    for i in range(h):
        print(''.join(ans[i]))