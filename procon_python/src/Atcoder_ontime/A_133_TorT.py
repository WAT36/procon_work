l = list(map(int,input().split()))
N = l[0]
A = l[1]
B = l[2]

if(N*A < B):
    print(N*A)
else:
    print(B)