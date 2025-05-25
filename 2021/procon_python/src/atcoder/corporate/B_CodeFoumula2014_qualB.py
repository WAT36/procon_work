n=input()
even=0
odd=0
for i in range(-1,-(len(n)+1),-1):
    if(i%2==0):
        even+=int(n[i])
    else:
        odd+=int(n[i])
print(even,odd)