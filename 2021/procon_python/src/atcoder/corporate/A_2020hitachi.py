s=input()
for i in range(0,len(s),2):
    if(s[i:i+2]!="hi"):
        print("No")
        break
else:
    print("Yes")