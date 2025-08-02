class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorts=''.join(sorted(list(s)))
        sortt=''.join(sorted(list(t)))
        return sorts == sortt
