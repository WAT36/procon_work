n,a,b=map(int,input().split())
s=[]
for i in range(n):
    s.append(int(input()))
max_s=max(s)
min_s=min(s)
sum_s=sum(s)

if(max_s==min_s):
    print(-1)
else:
    p=b/(max_s-min_s)
    q=a-(p/n)*sum_s
    print(str(p)+" "+str(q))