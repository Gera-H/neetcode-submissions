import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:        
        l = 1
        r = max(piles)
        minK = r
        while l <= r:
            m = (l + r) // 2
            totalH = 0
            for i in piles:
                totalH += math.ceil(i/m)
            if totalH < h:
                minK = m
                r = m - 1
            elif totalH > h:
                l = m + 1
            else:
                minK = m
                r = m - 1
        return minK