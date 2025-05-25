import bisect
n=int(input())
r=[]
b=[]
for i in range(n):
    r.append(list(map(int,input().split())))

for i in range(n):
    b.append(list(map(int,input().split())))

r.sort()
b.sort()

ans=0
for i in range(n):
    j=(n-1)-i
    bc,bd=list(zip(*b))
#    print(bc)
    bj_morethan_aj = bisect.bisect_left(bc, r[j][0])
    more_bi = b[bj_morethan_aj:]
    least_bd_k=-1
    least_bd=10000000
    for k in range(len(more_bi)):
        if(r[j][1] < more_bi[k][1] and more_bi[k][1] < least_bd):
            least_bd = more_bi[k][1]
            least_bd_k = k

    if(least_bd_k != -1):
        ans+=1
#        print(b[bj_morethan_aj+least_bd_k])
        del b[bj_morethan_aj+least_bd_k]
print(ans)