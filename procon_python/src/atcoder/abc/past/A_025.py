s=input()
n=int(input())
a=[]
for i in range(5):
    for j in range(5):
        a.append(s[i] + s[j])
a.sort()
print(a[n-1])