n=int(input())
r=0
b=0
for i in range(n):
    si=input()
    r+=si.count('R')
    b+=si.count('B')
print('TAKAHASHI' if r>b else 'AOKI' if b>r else 'DRAW')