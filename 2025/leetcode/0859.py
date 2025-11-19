class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        slist=sorted(s)
        goallist=sorted(goal)
        print(slist,goallist)
        if slist != goallist:
            return False
        diff=0
        countcheck=False
        for i in range(len(s)):
            if s.count(s[i]) >= 2:
                countcheck = True
            if s[i] != goal[i]:
                diff+=1
        if diff == 2:
            return True
        elif diff == 0 and countcheck:
            return True
        return False