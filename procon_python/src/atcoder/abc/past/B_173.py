import collections

def list_count(l):
    return collections.Counter(l)

n=int(input())
res=[]
for i in range(n):
    res.append(input())

res=list_count(res)

print("AC x {0}".format(res["AC"]))
print("WA x {0}".format(res["WA"]))
print("TLE x {0}".format(res["TLE"]))
print("RE x {0}".format(res["RE"]))


