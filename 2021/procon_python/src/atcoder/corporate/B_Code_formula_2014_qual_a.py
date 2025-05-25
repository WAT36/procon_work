a,b=map(int,input().split())
pin=['x' for _ in range(11)]
p=list(map(int,input().split()))
for pi in p:
    if(pi==0):
        pi=10
    pin[pi]='.'

q=list(map(int,input().split()))
for qi in q:
    if(qi==0):
        qi=10
    pin[qi]='o'

print(*pin[7:])
print(' ',end="")
print(*pin[4:7])
print('  ',end="")
print(*pin[2:4])
print('   ',end="")
print(pin[1])