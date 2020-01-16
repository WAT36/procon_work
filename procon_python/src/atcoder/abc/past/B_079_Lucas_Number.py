def lucas(n):
    l=[2,1]
    i=2
    while(i<=n):
        l.append(l[i-1]+l[i-2])
        i+=1
    return l[-1]

n=int(input())
print(lucas(n))