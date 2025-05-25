import sys
c=list(map(int,input().split()))
diffa=c[1]-c[0]
diffb=c[2]-c[1]

c=list(map(int,input().split()))
if(diffa!=(c[1]-c[0]) or diffb!=(c[2]-c[1])):
    print("No")
    sys.exit()

c=list(map(int,input().split()))
if(diffa!=(c[1]-c[0]) or diffb!=(c[2]-c[1])):
    print("No")
    sys.exit()

print("Yes")