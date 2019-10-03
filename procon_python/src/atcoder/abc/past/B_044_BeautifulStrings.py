w = input()
word = {}
l = len(w)

for i in range(l):
    n = word.get(w[i], 0)
    n = n+1
    word[w[i]] = n

flag = True
for i in word.values():
    if(i % 2 == 1):
        flag = False
        break

if(flag):
    print("Yes")
else:
    print("No")

