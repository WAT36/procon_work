s=int(input())
h=s//3600
m=(s//60)%60
se=s%60
print(str(h)+":"+str(m)+":"+str(se))