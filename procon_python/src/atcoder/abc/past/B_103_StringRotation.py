import sys
s=input()
t=input()
lists=list(s)
for _ in range(len(s)+1):
    s_top=lists.pop(0)
    lists.append(s_top)
    if(t==''.join(lists)):
        print("Yes")
        sys.exit()
print("No")
