import re
s=input()
s=' '+s+' '
n=int(input())
for i in range(n):
    ti=input()
    len_ti=len(ti)
    ti=ti.replace('*', '[a-z]')
    ti=' '+ti+' '
#    print(ti)
    s=re.sub(ti, ' '+('*'*len_ti)+' ', s)
    s=re.sub(ti, ' '+('*'*len_ti)+' ', s)
#    print(s)
print(s[1:len(s)-1])