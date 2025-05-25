# -*- coding:utf-8 -*-
l = list(map(int,input().split()))
W = l[0];
a = l[1];
b = l[2];

if(a+W < b):
    print(b-a-W);
elif(b+W < a):
    print(a-b-W);
else:
    print(0);