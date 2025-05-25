class Solution:
    def maximum69Number (self, num: int) -> int:
        str_num=list(str(num))
        for i in range(len(str_num)):
            if(str_num[i]=='6'):
                str_num[i]='9'
                break
        return int(''.join(str_num))

