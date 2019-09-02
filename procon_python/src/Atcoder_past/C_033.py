s=str(input())
zero_value=False
zero_item=0
plus_num=0
for i in range(len(s)):
    if(s[i] == "0"):
        zero_value=True
    elif(s[i] == "+"):
        plus_num+=1
        if(zero_value):
            zero_item+=1
        zero_value=False
if(zero_value):
    zero_item+=1
print(plus_num+1-zero_item)