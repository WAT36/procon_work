d=list(map(int,input().split()))
j=list(map(int,input().split()))
print(sum([max(d[i],j[i]) for i in range(len(d))]))
