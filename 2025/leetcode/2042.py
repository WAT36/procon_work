class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        ss=s.split(' ')
        now=-1
        for si in ss:
            if si.isnumeric():
                if now < int(si):
                    now=int(si)
                else:
                    return False
        return True