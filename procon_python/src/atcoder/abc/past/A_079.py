n=input()
if(len(list(set(n[:3])))==1 or len(list(set(n[1:])))==1):
    print("Yes")
else:
    print("No")