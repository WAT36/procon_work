s=input()
t=input()
sd=''.join(list(sorted(s)))
td=''.join(list(sorted(t,reverse=True)))
if(sd<td):
    print('Yes')
else:
    print('No')

