n=int(input())
a=list(map(int,input().split()))
i=[j for j in range(1,n+1)]
ai=zip(a,i)
ai=sorted(ai)
a,i=zip(*ai)
for j in range(n):
    print(i[j],end=" ")
print()