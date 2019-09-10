n,d,k=map(int,input().split())
l=[]
r=[]
for i in range(d):
    li,ri=map(int,input().split())
    l.append(li)
    r.append(ri)

s=[]
t=[]
for i in range(k):
    si,ti=map(int,input().split())
    s.append(si)
    t.append(ti)

for i in range(k):
    most_row=s[i]
    most_high=s[i]
    if(s[i] == t[i]):
        print(0)
        continue

    for j in range(d):
        if(l[j] <= most_row and most_row <= r[j]):
            most_row=l[j]

        if(l[j] <= most_high and most_high <= r[j]):
            most_high=r[j]

        if(most_row <= t[i] and t[i] <= most_high):
            print(j+1)
            break

