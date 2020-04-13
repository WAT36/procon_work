k=int(input())
fib=[1,1]
for i in range(k):
    fib.append(fib[-1]+fib[-2])
print(fib[-1],fib[-2])