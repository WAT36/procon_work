a,b,n=map(int,input().split())

def f(x):
    return (a*x)//b - a*(x//b)

print(f(min(b-1,n)))