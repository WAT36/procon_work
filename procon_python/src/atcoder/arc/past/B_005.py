x,y,w=input().split()
c=[]
for i in range(9):
    c.append(list(input()))
x=int(x)-1
y=int(y)-1

ans=[]

def goahead(y,x,w):
    ans.append(c[y][x])
    if(w=='R'):
        if(x==8):
            return y,x-1,'L'
        else:
            return y,x+1,'R'
    elif(w=='L'):
        if(x==0):
            return y,x+1,'R'
        else:
            return y,x-1,'L'
    elif(w=='U'):
        if(y==0):
            return y+1,x,'D'
        else:
            return y-1,x,'U'
    elif(w=='D'):
        if(y==8):
            return y-1,x,'U'
        else:
            return y+1,x,'D'
    elif(w=='RU'):
        if(y==0 and x==8):
            return y+1,x-1,'LD'
        elif(y==0):
            return y+1,x+1,'RD'
        elif(x==8):
            return y-1,x-1,'LU'
        else:
            return y-1,x+1,'RU'
    elif(w=='RD'):
        if(y==8 and x==8):
            return y-1,x-1,'LU'
        elif(y==8):
            return y-1,x+1,'RU'
        elif(x==8):
            return y+1,x-1,'LD'
        else:
            return y+1,x+1,'RD'
    elif(w=='LU'):
        if(y==0 and x==0):
            return y+1,x+1,'RD'
        elif(y==0):
            return y+1,x-1,'LD'
        elif(x==0):
            return y-1,x+1,'RU'
        else:
            return y-1,x-1,'LU'
    elif(w=='LD'):
        if(y==8 and x==0):
            return y-1,x+1,'RU'
        elif(y==8):
            return y-1,x-1,'LU'
        elif(x==0):
            return y+1,x+1,'RD'
        else:
            return y+1,x-1,'LD'


for i in range(4):
    y,x,w=goahead(y, x, w)

print(''.join(ans))
