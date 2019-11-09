n=int(input())
a=list(map(int,input().split()))
x=set()
for i in range(n):
    ai=a[i]
    while(ai%2==0):
        ai//=2
    x.add(ai)
print(len(x))