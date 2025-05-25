n=int(input())
c=[0 for _ in range(n+1)]
flag=[False for _ in range(n+1)]

for x in range(1,n+1):
    for y in range(1,n+1):
        for z in range(1,n+1):
            i=x*x + y*y + z*z + x*y + y*z + z*x
            if(i>n):
                break
            elif(x==y and y==z and z==x):
#                print(x,y,z,i)
                if(flag[i]):
                    pass
                else:
                    c[i]+=1
                    flag[i]=True
            else:
#                print(x,y,z,i)
                c[i]+=1
        j=x*x + y*y + 1 + x*y + y + x
        if(j>n):
            break
    k=x*x + 1 + 1 + x + 1 + x
    if(k>n):
        break

for i in range(1,n+1):
    print(c[i])