n=int(input())
h=n//3600
m=(n%3600)//60
s=n%60
print("{0:02d}:{1:02d}:{2:02d}".format(h,m,s))
