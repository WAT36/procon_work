n=int(input())
s=input()

x=0
max_x=0

for si in list(s):
    if(si=="I"):
        x+=1
    else:
        x-=1
    if(max_x<x):
        max_x=x
print(max_x)