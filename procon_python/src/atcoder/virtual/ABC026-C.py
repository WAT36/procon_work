n=int(input())
subord=[[] for i in range(n+1)]
for i in range(2,n+1):
    bi=int(input())
    subord[bi].append(i)

sal=[0 for i in range(n+1)]
for i in range(n,0,-1):
    sal_i=[]
    for j in subord[i]:
        sal_i.append(sal[j])

    if(len(sal_i)==0):
        sal[i]=1
    else:
        sal[i]=max(sal_i)+min(sal_i)+1


print(sal[1])