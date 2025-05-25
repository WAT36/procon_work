import statistics
n=int(input())
a=list(map(int,input().split()))
b=[a[i]-(i+1) for i in range(n)]
b_median=statistics.median(b)
ans=int(sum([abs(b[i]-b_median) for i in range(n)]))
print(ans)