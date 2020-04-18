n,x=map(int,input().split())


b=[1]
p=[1]
for i in range(n):
    b.append(2*b[-1]+3)
    p.append(2*p[-1]+1)

def f(N,X):
    if N==0:
        return 0 if X<=0 else 1
    elif X==1:
        return 0
    elif 1<X and X<=b[N-1]+1:
        return f(N-1,X-1)
    elif X==b[N-1]+2:
        return p[N-1]+1
    else:
        return p[N-1]+1+f(N-1,X-2-b[N-1])

print(f(n,x))