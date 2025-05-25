nm = list(map(int,input().split()))
N = nm[0]
M = nm[1]

py ={}
iy ={}
yp ={}

for i in range(M):
    PY = list(map(int,input().split()))
    P = PY[0]
    Y = PY[1]
    iy[i] = Y
    yp[Y] = P
    if(P in py):
        temp = py[P]
        temp.append(Y)
        temp.sort()
        py[P] = temp
    else:
        temp = []
        temp.append(Y)
        py[P] = temp

for i in range(M):
    y = iy[i]
    p = yp[y]
    x = py[p].index(y)
    pref = ("000000" + str(p))[-6:]
    X = ("000000" + str(x+1))[-6:]
    print(pref + X)
