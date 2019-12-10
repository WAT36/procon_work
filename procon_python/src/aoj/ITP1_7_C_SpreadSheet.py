r,c=map(int,input().split())
sheet=[]
for i in range(r):
    sheet.append(list(map(int,input().split())))

c_ans=[0 for _ in range(c)]
for i in range(r):
    for j in range(c):
        c_ans[j]+=sheet[i][j]
    sheet[i].append(sum(sheet[i]))
c_ans.append(sum(c_ans))
sheet.append(c_ans)

for i in range(len(sheet)):
    for j in range(len(sheet[i])):
        print(sheet[i][j],end="")

        if(j<len(sheet[i])-1):
            print(" ",end="")
    print()
