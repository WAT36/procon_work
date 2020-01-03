a,b=input().split()
ab=int(a+b)
rootab=ab**(1/2)//1
if(ab==rootab**2):
    print("Yes")
else:
    print("No")
