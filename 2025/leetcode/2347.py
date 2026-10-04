class Solution:
    def bestHand(self, ranks: list[int], suits: list[str]) -> str:
        if len(list(set(suits)))==1:
            return "Flush"
        if len(list(set(ranks)))<=3:
            for r in list(set(ranks)):
                if ranks.count(r)==1:
                    continue
                elif ranks.count(r)>=3:
                    return "Three of a Kind"
            return "Pair"
        if len(list(set(ranks)))<=4:
            return "Pair"
        return "High Card"
