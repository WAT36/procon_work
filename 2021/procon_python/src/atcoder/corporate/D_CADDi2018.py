n=int(input())
a=[]
even=True
for i in range(n):
    ai=int(input())
    a.append(ai)
    if(ai%2!=0):
        even=False
print('second' if even else 'first')