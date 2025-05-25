h,w,k=map(int,input().split())
s=[]
for i in range(h):
    s.append(input())
ans=[]
strawc=0
reexe=False
for i in range(h):
    if(s[i].count("#")==0):
        if(i==0):
            reexe=True
            ans.append(s[i])
        else:
            ans.append(ans[i-1])
    elif(s[i].count("#")==1):
        strawc+=1
        ans.append([str(strawc) for _ in range(w)])
    else:
        nocount=0
        ans_i=[]
        for j in range(w):
            if(s[i][j]=="#"):
                strawc+=1
                for _ in range(nocount+1):
                    ans_i.append(str(strawc))
                nocount=0
            else:
                nocount+=1
        for _ in range(nocount):
            ans_i.append(str(strawc))
        ans.append(ans_i)

if(reexe):
    for i in range(h):
        j=h-1-i
        if(ans[j].count(".")>0):
            ans[j]=ans[j+1]

for i in range(h):
    for j in range(w):
        print(ans[i][j],end=" ")
    print()