n,q=map(int,input().split())
othello=[0 for i in range(n+1)]
for i in range(q):
    l,r=map(int,input().split())
    othello[l-1]+=1
    othello[r]-=1
count=0
for i in range(n):
    count+=othello[i]
    if(count%2==0):
        print(0,end="")
    else:
        print(1,end="")
print()