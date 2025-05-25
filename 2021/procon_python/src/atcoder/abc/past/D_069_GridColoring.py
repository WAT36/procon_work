h,w=map(int,input().split())
n=int(input())
a=list(map(int,input().split()))
ans=[]
i=0
rest=a[i]
for j in range(h):
    ans_j=[]
    for k in range(w):
        if(rest==0):
            i+=1
            rest=a[i]

        if(j%2==0):
            ans_j.append(i+1)
            rest-=1
        else:
            ans_j.insert(0, i+1)
            rest-=1
    ans.append(ans_j)

for i in range(len(ans)):
    for j in range(len(ans[i])):
        print(ans[i][j],end=" ")
    print()