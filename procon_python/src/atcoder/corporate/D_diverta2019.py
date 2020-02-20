n=int(input())
#約数列挙
div=[]
for i in range(1,int((n**0.5)//1)+1):
    if(n%i==0):
        div.append(i)
        div.append(n//i)
div=sorted(list(set(div)))

ans=[0]
#iをmで割った商とiをmで割った余りが等しいときのm
#i//m + i%m
#m*x + x = i
#x = i/(m+1)
#m+1はiの約数
#xはm未満
for divi in div:
    m=divi-1
    if(n//divi < m):
        ans.append(m)
print(ans)
print(sum(ans))
