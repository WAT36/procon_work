n=int(input())
s=[]
for _ in range(n):
    s.append(input())

s.sort(key=lambda x:x[::-1])

for i in range(n):
    print(s[i])