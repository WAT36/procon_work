n=int(input())
keta=-(-n//9)
num=n%9 if n%9!=0 else 9
print(int(str(num)*keta))
