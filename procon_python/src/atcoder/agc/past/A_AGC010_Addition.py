# -*- coding:utf-8 -*-
N = int(input())
A = list(map(int,input().split()))
sum = sum(A)

if(sum%2 == 0):
    print("YES");
else:
    print("NO");