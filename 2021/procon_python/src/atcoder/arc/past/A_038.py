n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
a=a[::2]
print(sum(a))

