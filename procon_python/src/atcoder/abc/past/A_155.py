abc=list(map(int,input().split()))
set_abc=set(abc)
if(len(set_abc)==2):
    print("Yes")
else:
    print("No")