abc = list(map(int,input().split()))
abc.sort()
print(abc[0] + (abc[2]*10 + abc[1]))
