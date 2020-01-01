#解説を見た　何気にムズイ
import re
def bubbleSort(c):
    flag=True
    while(flag):
        flag=False
        for i in range(len(c)-1):
            if(c[i][1] > c[i+1][1]):
                c[i],c[i+1] = c[i+1],c[i]
                flag=True
    return c

def selectionSort(c):
    for i in range(len(c)):
        minj=i
        for j in range(i,len(c)):
            if(c[j][1] < c[minj][1]):
                minj=j
        if(i!=minj):
            c[i],c[minj]=c[minj],c[i]
    return c

n=int(input())
cards=list(input().split())
c=[]
for i in range(n):
    c.append([cards[i][0],int(cards[i][1])])
c2=c.copy()

bubble=bubbleSort(c)
bubble_str=re.sub("[\[\]\,]","",str(bubble))
bubble_str=re.sub("\' ","",bubble_str)
print(re.sub("\'","",bubble_str))
print("Stable")

select=selectionSort(c2)
select_str=re.sub("[\[\]\,]","",str(select))
select_str=re.sub("\' ","",select_str)
print(re.sub("\'","",select_str))
if(bubble_str == select_str):
    print("Stable")
else:
    print("Not stable")
