s = list(str(input()))
t = list(str(input()))

s.sort()
t.sort()
t.reverse()

def cond1(s,t):
    n = len(s)
    m = len(t)
    if(n >= m):
        return False
    else:
        for i in range(n):
            if(ord(s[i]) != ord(t[i])):
                return False
        return True

def cond2(s,t):
    m = min(len(s),len(t))
    for i in range(m):
        if(ord(s[i]) < ord(t[i])):
            return True
        elif(ord(s[i]) > ord(t[i])):
            return False
    return False

ans = (cond1(s,t) or cond2(s,t))

if(ans):
    print("Yes")
else:
    print("No")