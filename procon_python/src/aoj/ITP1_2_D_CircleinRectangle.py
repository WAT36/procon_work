w,h,x,y,r=map(int,input().split())
if(r<=x and x<=w-r and r<=y and y<=h-r):
    print("Yes")
else:
    print("No")