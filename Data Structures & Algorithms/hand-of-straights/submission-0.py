class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = {}
        hand.sort()
        f =[]

        for card in hand:
            count[card] = count.get(card, 0) + 1
        
        for card in hand:
            if count[card] == 0:
                continue
            for i in range(card, card+groupSize):
                if count.get(i, 0) == 0:
                    return False
                count[i] -=1
        return True



