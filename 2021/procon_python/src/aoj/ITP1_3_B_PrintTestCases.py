x=-1
c=[]
while(x!=0):
    x=int(input())
    c.append(x)

for i in range(len(c)-1):
    print("Case " + str(i+1)+": "+str(c[i]))