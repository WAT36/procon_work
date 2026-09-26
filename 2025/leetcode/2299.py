class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        alpha='abcdefghijklmnopqrstuvwxyz'
        digit='0123456789'
        speci='!@#$%^&*()-+'
        
        if len(password)<8:
            return False
        if len(list(set(list(alpha)) & set(list(password))))==0:
            return False
        if len(list(set(list(alpha.upper())) & set(list(password))))==0:
            return False
        if len(list(set(list(digit)) & set(list(password))))==0:
            return False
        if len(list(set(list(speci)) & set(list(password))))==0:
            return False
        for i in range(len(password)-1):
            if password[i]==password[i+1]:
                return False
        return True

