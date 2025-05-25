xa,ya,xb,yb,xc,yc=map(int,input().split())
print(abs((yb-ya)*(xc-xa) - (xb-xa)*(yc-ya))/2)