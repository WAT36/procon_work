class Solution:
    def digitCount(self, num: str) -> bool:
        ln=list(num)
        for i in range(len(num)):
            if ln.count(str(i)) != int(num[i]):
                return False
        return True