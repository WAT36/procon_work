import numpy as np
h,w,k=map(int,input().split())
c=[]
blacks=0
for hi in range(h):
    c.append(list(input()))
    blacks+=c[-1].count('#')
c=np.array(c)
#print(c)
x=h+w
bx=2**x
ans=0
max_ansi=0
for i in range(bx):
    bin_x=bin(i)[2:].zfill(x)
#    print(bin_x)
    line=[]
    row=[]
    ansi=0
    for j in range(h):
        if(bin_x[j]=='1'):
            line.append(j)
    for j in range(w):
        if(bin_x[h+j]=='1'):
            row.append(j)
    line=np.array(line)
    row=np.array(row)
    not_line=np.array(list(set([i for i in range(h)]) - set(line)))

    for j in range(x):
        if(bin_x[j]=='1'):
            if(j<h):
                ansi+=np.count_nonzero(c[j,:]=='#')
            elif(len(not_line)>0):
                m=j-h
                ansi+=np.count_nonzero(c[not_line[:],m]=='#')
    ansi=blacks-ansi
    if(ansi==k):
        ans+=1
#    print(ansi,ans,line,row,not_line)
print(ans)

