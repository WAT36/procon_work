a,b=map(int,input().split())
if(a==b):
    print("Draw")
elif(b!=1 and (a>b or a==1)):
    print("Alice")
else:
    print("Bob")