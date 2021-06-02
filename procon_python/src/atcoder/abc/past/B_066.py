s=input()
for i in range(len(s)-2,0,-2):
    if(s[:i//2] == s[i//2:i]):
        print(i)
        break
