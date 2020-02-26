c=[]
for _ in range(4):
    c.append(list(input().split()))

for i in range(3,-1,-1):
    print(c[i][3],c[i][2],c[i][1],c[i][0])