l = list(map(int,input().split()))
A = l[0];
B = l[1];

if(A%B == 0):
    print(-1)
else:
    xa = A*2;

    while ((xa%B == 0) and (xa < 10**18)):
        xa += A;

    if(xa > 10**18):
        print(-1);
    else:
        print(xa);