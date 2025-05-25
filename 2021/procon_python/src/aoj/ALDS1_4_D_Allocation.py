n,k=map(int,input().split())
w=[0 for _ in range(100001)]
for i in range(n):
    w[i]=int(input())

#最大積載量pとした時のチェック
def check(p):
    sumw=0
    idx=0

    for i in range(k):
        sumw=0
        while(w[idx]+sumw<=p):
            sumw+=w[idx]
            idx+=1
            if(idx==n):
#                print("{0}台で運べる:w[{1}]まで、 積載量{2} 最大積載量{3} ".format(i+1,idx,sumw,p))
                return True
#            print("runT:{0} {1} {2} k={3}".format(idx,sumw,p,i))
#        print("{0}台目:w[{1}]まで、 積載量{2} 最大積載量{3}".format(i+1,idx-1,sumw,p))
#    print("運べない:w[{0}]でアウト 積載量{1} 最大積載量{2} k={3}".format(idx,sumw,p,k-1))
    return False

left=0
right=100000*10000

while(right - left > 1):
    mid = (left + right)//2
#    print("最大積載量p:{0}".format(mid))
    if(check(mid)):
        right=mid
    else:
        left=mid
#    print("main:left:{0} right:{1} mid:{2}".format(left,right,mid))

print(right)
