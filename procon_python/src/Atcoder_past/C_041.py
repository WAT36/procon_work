N = int(input())
a = list(map(int,input().split()))
b = list(range(1,len(a)+1))
c = zip(a,b)
c = reversed(sorted(c))
b,a = zip(*c)
for i in range(N):
    print(a[i])