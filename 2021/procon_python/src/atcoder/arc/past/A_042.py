n,m=map(int,input().split())
thread=set([i for i in range(1,n+1)])
a=[]
for i in range(m):
    a.append(int(input()))

checked_a=set()
for i in range(-1,-m-1,-1):
    if(a[i] not in checked_a):
        print(a[i])
        checked_a.add(a[i])

thread=sorted(list(thread-checked_a))
for i in range(len(thread)):
    print(thread[i])
