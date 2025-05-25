strn=input()
n=int(strn)
fn=0
for i in range(len(strn)):
    fn+=int(strn[i])
if(n%fn==0):
    print("Yes")
else:
    print("No")
