import re
s=input()
print(re.search(r'\d+',s).group())
