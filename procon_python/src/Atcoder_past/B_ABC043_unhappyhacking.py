s = input()
t = []

for i in range(len(s)):
    if(s[i] == "B"):
        if(len(t) > 0):
            del t[-1]
    else:
        t.append(s[i])

for i in range(len(t)):
    print(t[i],end="")