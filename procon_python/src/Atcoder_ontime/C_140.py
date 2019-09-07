n=int(input())
b=list(map(int,input().split()))
a=[]
a.append(b[0])
for i in range(n-1):
    a[i] = b[i] if a[i] > b[i] else a[i]
    a.append(b[i])
#    print(a)
print(sum(a))