w=input()
boin=['a','i','u','e','o']
ans=[]
for wi in w:
    if(wi not in boin):
        ans.append(wi)
print(''.join(ans))