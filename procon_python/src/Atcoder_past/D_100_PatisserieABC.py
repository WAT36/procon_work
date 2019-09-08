n,m=map(int,input().split())
x=[]
y=[]
z=[]
for i in range(n):
    xi,yi,zi=map(int,input().split())
    x.append(xi)
    y.append(yi)
    z.append(zi)

def minus(x):
    return -1 * x

ans=0
for i in range(2):
    temp_x = x
    if(i==1):
        temp_x = list(map(minus,x))
    for j in range(2):
        temp_y = y
        if(j==1):
            temp_y = list(map(minus,y))
        for k in range(2):
            temp_z = z
            if(k==1):
                temp_z = list(map(minus,z))

            xyz = [temp_x[l] + temp_y[l] + temp_z[l] for l in range(n)]
            xyz.sort()
            temp_sum=0
            for h in range(n-m,n):
                temp_sum+=xyz[h]
            if(ans < temp_sum):
                ans = temp_sum
print(ans)
