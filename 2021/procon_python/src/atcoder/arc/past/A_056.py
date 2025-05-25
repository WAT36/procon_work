a,b,k,l=map(int,input().split())
na=-(-k//l)
nb=k//l
print(min(a*k,b*na,b*nb+(k-l*nb)*a))