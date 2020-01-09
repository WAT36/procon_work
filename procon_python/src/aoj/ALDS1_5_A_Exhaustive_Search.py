n=int(input())
a=list(map(int,input().split()))
q=int(input())
m=list(map(int,input().split()))

ans=[0]
for i in range(n):
    ans_bkup=ans.copy()
    ans=list(map(lambda x: x+a[i],ans))
#    print(ans,ans_bkup)
    ans.extend(ans_bkup)
    ans=list(set(ans))

for i in range(q):
    if(m[i] in ans):
        print("yes")
    else:
        print("no")