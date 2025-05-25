w,h,n=map(int,input().split())
white_mostleft=0
white_mostright=w
white_mostup=h
white_mostdown=0

for _ in range(n):
    x,y,a=map(int,input().split())
    if(a==1 and white_mostleft < x):
        white_mostleft=x
    elif(a==2 and white_mostright > x):
        white_mostright=x
    elif(a==3 and white_mostup > h-y):
        white_mostup = h-y
    elif(a==4 and white_mostdown < h-y):
        white_mostdown = h-y

ans=max(0,white_mostright-white_mostleft) * max(0,white_mostup-white_mostdown)
print(ans)
