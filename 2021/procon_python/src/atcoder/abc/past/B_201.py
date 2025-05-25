n=int(input())
m=[]
for _ in range(n):
    s,t=list(input().split())
    m.append([s,int(t)])

m.sort(key=lambda x:x[1])
print(m[-2][0])