n=int(input())
a=[]
for _ in range(n):
    a.append(int(input()))
a=sorted(list(set(a)))
print(a[-2])