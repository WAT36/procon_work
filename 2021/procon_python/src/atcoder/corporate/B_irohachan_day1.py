s=input()
k=int(input())
k=k%len(s)
print(s[k:]+s[:k])
