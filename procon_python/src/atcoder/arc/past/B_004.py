n=int(input())
d=[]
for i in range(n):
    d.append(int(input()))
sum_d=sum(d)
print(sum_d)
max_d=max(d)
if(max_d>sum_d-max_d):
    print(max_d-(sum_d-max_d))
else:
    print(0)