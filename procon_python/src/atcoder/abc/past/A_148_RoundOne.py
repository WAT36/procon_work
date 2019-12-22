a=int(input())
b=int(input())
que=[a,b]
ans=[i for i in range(1,4) if i not in que]
print(ans[0])