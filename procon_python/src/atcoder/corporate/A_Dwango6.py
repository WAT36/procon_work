n=int(input())
s=[]
t=[]
for i in range(n):
    st=list(input().split())
    s.append(st[0])
    t.append(int(st[1]))
x=input()

print(sum(t[s.index(x)+1:]))

