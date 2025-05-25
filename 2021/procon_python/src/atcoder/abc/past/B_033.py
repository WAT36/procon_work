n=int(input())
s=[]
p=[]
for _ in range(n):
    si,pi=input().split()
    s.append(si)
    p.append(int(pi))
sum_p=sum(p)
for i in range(n):
    if(p[i]>(sum_p//2)):
        print(s[i])
        break
else:
    print('atcoder')
