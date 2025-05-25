import re
N = int(input())
regex = r'.*okyo.*ech.*'
pattern = re.compile(regex)
ans = []
for i in range(N):
    s = str(input())
    a = pattern.fullmatch(s)
    ans.append("No" if a is None else "Yes")

for i in range(N):
    print(ans[i])