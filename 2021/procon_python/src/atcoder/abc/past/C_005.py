t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

i = 0
j = 0
while(True):
   if(j >= len(b)):
       print("yes")
       break
   elif(i >= len(a)):
       print("no")
       break
   elif(b[j] < a[i]):
       print("no")
       break
   elif(b[j] - a[i] <= t):
       i += 1
       j += 1
   else:
       i += 1
