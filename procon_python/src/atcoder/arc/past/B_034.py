n=int(input())

ans=[]
for i in range(max(n-154,0),n):
    fi=sum(list(map(int,list(str(i)))))
    if(i+fi==n):
        ans.append(i)

print(len(ans))
for i in range(len(ans)):
    print(ans[i])

